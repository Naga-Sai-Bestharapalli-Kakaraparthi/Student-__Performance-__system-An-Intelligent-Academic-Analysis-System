def predict(student_data):
    attendance = student_data.get("attendance", 0)
    study_hours = student_data.get("study_hours", 0)
    quiz_score = student_data.get("quiz_score", 0)
    assignment_score = student_data.get("assignment_score", 0)
    cumulative_quiz_score = student_data.get("cumulative_quiz_score", 0)

    predicted_score = (
        quiz_score * 0.3 +
        assignment_score * 0.3 +
        cumulative_quiz_score * 0.2 +
        attendance * 0.1 +
        (study_hours / 6) * 100 * 0.1
    )

    predicted_score = round(min(100, max(0, predicted_score)), 2)

    if predicted_score >= 80:
        risk = "Low"
    elif predicted_score >= 60:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "predicted_score": predicted_score,   # ✅ KEY EXISTS AGAIN
        "risk": risk
    }
