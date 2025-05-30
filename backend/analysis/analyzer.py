from models.roberta_model import get_verdict

def analyze_text(text):
    result = get_verdict(text)  # Make sure it returns a dict with "verdict" and "confidence"

    verdict = result["verdict"]
    confidence = result["confidence"]

    # Dynamic reason based on verdict + confidence
    if verdict == "FAKE":
        if confidence > 0.9:
            reason = "Highly confident in detecting fake content due to misleading language patterns."
        elif confidence > 0.7:
            reason = "Likely fake; content shows signs of manipulation or exaggeration."
        else:
            reason = "Possibly fake, but evidence is limited or unclear."
    else:  # Real
        if confidence > 0.9:
            reason = "Strong indications of authenticity from credible patterns."
        elif confidence > 0.7:
            reason = "Seems real but cross-verification is suggested."
        else:
            reason = "Likely real, but confidence is moderate."

    return {
        "claim": text[:200] + "...",
        "verdict": {
            "verdict": verdict,
            "confidence": confidence
        },
        "reason": reason
    }
