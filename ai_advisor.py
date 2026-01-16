def generate_advice(student_data, prediction):
    score = prediction["predicted_score"]
    risk = prediction["risk"]

    explanation = []
    advice = []

    # ---- Explanation ----
    if score >= 80:
        explanation.append("Student is performing very well academically.")
    elif score >= 60:
        explanation.append("Student performance is average with scope for improvement.")
    else:
        explanation.append("Student performance is currently below expectations.")

    if risk == "High":
        explanation.append("The student is at high academic risk.")
    elif risk == "Medium":
        explanation.append("The student shows moderate academic risk.")
    else:
        explanation.append("The student shows low academic risk.")

    # ---- Advice ----
    if risk == "High":
        advice.extend([
            "Revise core concepts daily.",
            "Increase focused study hours.",
            "Attempt practice quizzes regularly."
        ])
    elif risk == "Medium":
        advice.extend([
            "Maintain consistency in studies.",
            "Strengthen weak topics.",
            "Practice weekly assessments."
        ])
    else:
        advice.extend([
            "Continue the current study strategy.",
            "Attempt advanced problems.",
            "Maintain regular revision."
        ])

    return {
        "explanation": explanation,
        "advice": advice
    }
