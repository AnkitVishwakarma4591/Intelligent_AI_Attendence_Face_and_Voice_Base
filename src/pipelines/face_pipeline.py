import dlib
import numpy as np
import streamlit as st
import face_recognition_models

from src.database.db import get_all_students


# A lower distance is deliberately used here than the commonly used 0.6
# default. Attendance should reject uncertain matches rather than guess.
FACE_DISTANCE_THRESHOLD = 0.45
FACE_MATCH_MARGIN = 0.04


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    face_recognizer = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector, shape_predictor, face_recognizer


def get_face_embeddings(image_np):
    detector, shape_predictor, face_recognizer = load_dlib_models()
    image_np = np.asarray(image_np)
    faces = detector(image_np, 1)
    embeddings = []

    for face in faces:
        shape = shape_predictor(image_np, face)
        descriptor = face_recognizer.compute_face_descriptor(image_np, shape, 1)
        embeddings.append(np.asarray(descriptor, dtype=np.float64))
    return embeddings


def _coerce_embeddings(raw_embedding):
    """Normalize embeddings stored as arrays or JSON-like lists."""
    if raw_embedding is None:
        return []
    if isinstance(raw_embedding, str):
        # Some Supabase schemas return JSON columns as serialized text.
        import json
        try:
            raw_embedding = json.loads(raw_embedding)
        except (TypeError, ValueError):
            return []

    try:
        values = np.asarray(raw_embedding, dtype=np.float64)
    except (TypeError, ValueError):
        return []

    if values.ndim == 1:
        values = values.reshape(1, -1)
    if values.ndim != 2 or values.shape[1] != 128:
        return []
    if not np.isfinite(values).all():
        return []
    return [row for row in values]


@st.cache_resource
def get_trained_model():
    """Return the enrolled face templates keyed by student ID."""
    templates = {}
    for student in get_all_students() or []:
        student_id = student.get("student_id")
        try:
            student_id = int(student_id)
        except (TypeError, ValueError):
            continue

        embeddings = _coerce_embeddings(student.get("face_embedding"))
        if embeddings:
            templates.setdefault(student_id, []).extend(embeddings)
    return templates


def train_classifier():
    # Retain the existing public function name used after registration.
    get_trained_model.clear()
    return bool(get_trained_model())


def predict_attendance(class_image_np):
    """Return only confident, unambiguous matches for faces in an image."""
    encodings = get_face_embeddings(class_image_np)
    templates = get_trained_model()
    if not templates:
        return {}, [], len(encodings)

    matches = {}
    for encoding in encodings:
        encoding = np.asarray(encoding, dtype=np.float64).reshape(-1)
        if encoding.size != 128 or not np.isfinite(encoding).all():
            continue

        student_distances = []
        for student_id, references in templates.items():
            distance = min(float(np.linalg.norm(encoding - reference)) for reference in references)
            student_distances.append((distance, student_id))

        student_distances.sort()
        best_distance, best_student_id = student_distances[0]
        second_best = student_distances[1][0] if len(student_distances) > 1 else float("inf")

        # A lone enrolled student still needs a close match. With several
        # students, also reject near ties instead of arbitrarily choosing one.
        if best_distance <= FACE_DISTANCE_THRESHOLD and second_best - best_distance >= FACE_MATCH_MARGIN:
            matches[best_student_id] = True

    return matches, sorted(templates), len(encodings)
