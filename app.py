import streamlit as st

from predictor import predict
from ai_advisor import generate_advice
from study_plan import generate_study_plan
from progress_tracker import track_progress
from risk_score import calculate_risk

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance AI",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(to bottom right, #f4f8ff, #e8f0ff);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Center title */
    h1 {
        text-align: center;
        color: #1f3c88;
        font-weight: 700;
    }

    /* Section headers */
    h2, h3 {
        color: #2a4d9b;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #1f3c88;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        font-size: 16px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #163172;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.title("🎓 Student Performance AI System")
st.markdown(
    "<p style='text-align:center; font-size:18px;'>AI-driven academic performance analysis and guidance</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.header("📥 Student Input Details")

attendance = st.slider("Attendance (%)", 0, 100, 60)
study_hours = st.slider("Study Hours per Day", 0.0, 6.0, 2.0, 0.5)
quiz_score = st.slider("Quiz Score", 0, 100, 70)
assignment_score = st.slider("Assignment Score", 0, 100, 75)
cumulative_quiz_score = st.slider("Cumulative Quiz Score", 0, 100, 72)
previous_score = st.slider("Previous Score", 0, 100, 65)

subjects = ["Maths", "Physics", "Programming"]

st.markdown("---")

# ---------------- RUN BUTTON ----------------
run = st.button("🚀 Run AI Analysis")

# ---------------- OUTPUT SECTION ----------------
if run:
    student_data = {
        "attendance": attendance,
        "study_hours": study_hours,
        "quiz_score": quiz_score,
        "assignment_score": assignment_score,
        "cumulative_quiz_score": cumulative_quiz_score,
        "previous_score": previous_score,
        "subjects": subjects
    }

    prediction = predict(student_data)
    advisor = generate_advice(student_data, prediction)
    study_plan = generate_study_plan(student_data, prediction)
    progress = track_progress(previous_score, prediction)
    risk = calculate_risk(prediction)

    st.markdown("---")
    st.header("📊 Prediction Result")
    st.metric("Predicted Score", prediction["predicted_score"])
    st.metric("Risk Level", prediction["risk"])

    st.header("🧠 Explanation")
    for e in advisor["explanation"]:
        st.write("•", e)

    st.header("✅ Advice")
    for a in advisor["advice"]:
        st.write("•", a)

    st.header("📅 Personalized Study Plan")
    for day, task in study_plan.items():
        st.write(f"**{day}**: {task}")

    st.header("📈 Progress Tracking")
    st.write(progress)

    st.header("🎯 Risk Assessment")
    st.write(risk)
