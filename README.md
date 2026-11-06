# SnapClass — AI Attendance

**Live app:** [snapclass-attendance-ankit.streamlit.app](https://snapclass-attendance-ankit.streamlit.app/)

SnapClass is a Streamlit attendance app for teachers and students. Teachers can manage classes, collect classroom photos or audio, review AI-generated attendance, and save attendance records. Students create a profile using a face photo, enroll in subjects, and view their attendance history.

## Features

- Teacher registration and password login.
- Student profile registration and sign-in using face recognition.
- Face-based classroom attendance from uploaded photos or camera captures.
- Optional voice enrollment and voice-based attendance.
- Subject creation, enrollment by subject code, and QR join links.
- Attendance review before saving records to Supabase.
- Student attendance summaries and teacher attendance reports.

## Screenshots

### Home page

![SnapClass home page](src/images/Home%20page.png)

### Student login

![SnapClass student login](src/images/student%20login.png)

### Teacher login

![SnapClass teacher login](src/images/teacher%20login.png)

## Technology

- Python 3.12
- Streamlit
- Supabase for application data
- dlib face embeddings and scikit-learn / NumPy matching utilities
- Resemblyzer and librosa for voice embeddings and audio processing
- Pillow and Segno for image handling and QR codes

## Run locally

1. Clone the repository and enter its directory.

   ```powershell
   git clone https://github.com/AnkitVishwakarma4591/Intelligent-AI-Attendence---Face-Voice.git
   cd Intelligent-AI-Attendence---Face-Voice
   ```

2. Create and activate a Python 3.12 virtual environment.

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux, activate it with `source .venv/bin/activate`.

3. Install dependencies.

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   Some audio and face-recognition dependencies include native components and may require platform-specific build tools or compatible wheels.

4. Create `.streamlit/secrets.toml` with your Supabase project credentials:

   ```toml
   SUPABASE_URL = "https://your-project.supabase.co"
   SUPABASE_KEY = "your-supabase-key"
   ```

   Keep this file private. It is excluded from Git by `.gitignore`.

5. Start the app.

   ```bash
   streamlit run app.py
   ```

## Supabase data model

The app expects these tables and relationships. Use generated integer primary keys for `teacher_id`, `student_id`, and `subject_id`; add foreign keys for the relationships shown below.

| Table | Fields used by the app |
| --- | --- |
| `teachers` | `teacher_id`, `username`, `password`, `name` |
| `students` | `student_id`, `name`, `face_embedding`, `voice_embedding` |
| `subjects` | `subject_id`, `subject_code`, `name`, `section`, `teacher_id` |
| `subject_students` | `student_id`, `subject_id` |
| `attendance_logs` | `student_id`, `subject_id`, `timestamp`, `is_present` |

Store `face_embedding` and `voice_embedding` as JSON arrays (for example, `jsonb` columns). Configure Supabase foreign-key relationships between `subjects.teacher_id` and `teachers.teacher_id`, and from `subject_students` and `attendance_logs` to the relevant student and subject rows. Subject codes should be unique if they are used as join codes.

## Project layout

```text
app.py                         Streamlit entry point and portal routing
src/
  components/                  Reusable headers, cards, and dialogs
  database/                    Supabase client and database operations
  pipelines/                   Face and voice recognition
  screens/                     Home, teacher, and student screens
  ui/                          Shared CSS and page styling
```

## Biometric data

Student registration stores face embeddings and may store voice embeddings in the configured Supabase project. Use this project only with appropriate notice, consent, access controls, and retention practices for biometric data. Attendance results should be reviewed before saving.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
