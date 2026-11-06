import streamlit as st
from PIL import Image
import hashlib
from io import BytesIO


def _store_photo_once(photo_bytes):
    """Prevent Streamlit reruns from appending the same selected file again."""
    photo_key = hashlib.sha256(photo_bytes).hexdigest()
    stored_keys = st.session_state.setdefault('attendance_image_keys', set())
    if photo_key in stored_keys:
        return False
    st.session_state.setdefault('attendance_images', []).append(
        Image.open(BytesIO(photo_bytes)).convert('RGB')
    )
    stored_keys.add(photo_key)
    return True


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'



    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo:
            if _store_photo_once(cam_photo.getvalue()):
                st.toast('Photo Captured')
                st.rerun()


    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader( 'choose image files', type=['jpg', 'png', 'jpeg' ], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            added = False
            for f in uploaded_files:
                added = _store_photo_once(f.getvalue()) or added
            if added:
                st.toast('Photo Uploaded Successfully')
                st.rerun()

    st.divider()
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()
