def calculate_risk(prediction):
    score = prediction["predicted_score"]
    risk = prediction["risk"]

    if risk == "Low":
        confidence = "85%"
    elif risk == "Medium":
        confidence = "60%"
    else:
        confidence = "30%"

    return {
        "risk": risk,
        "confidence": confidence
    }
