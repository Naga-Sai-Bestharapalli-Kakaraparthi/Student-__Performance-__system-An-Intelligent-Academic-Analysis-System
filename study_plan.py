def generate_study_plan(student_data, prediction):
    score = prediction["predicted_score"]
    subjects = student_data.get("subjects", ["Maths", "Physics", "Programming"])

    if score < 60:
        hours = 3
    elif score < 80:
        hours = 2.5
    else:
        hours = 2

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    plan = {}

    for i, day in enumerate(days):
        if day == "Sunday":
            plan[day] = "Revision + Mock Test (2 hrs)"
        else:
            subject = subjects[i % len(subjects)]
            plan[day] = f"{subject} – {hours} hrs (concepts + practice)"

    return plan
