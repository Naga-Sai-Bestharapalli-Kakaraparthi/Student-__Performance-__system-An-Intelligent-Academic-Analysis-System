def track_progress(previous_score, prediction):
    current_score = prediction["predicted_score"]
    change = current_score - previous_score

    if change > 5:
        trend = "Improving"
    elif change < -5:
        trend = "Declining"
    else:
        trend = "Stable"

    return {
        "previous_score": previous_score,
        "current_score": current_score,
        "change": round(change, 2),
        "trend": trend
    }
