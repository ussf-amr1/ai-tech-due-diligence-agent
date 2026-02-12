def make_recommendation(risks):
    """
    Generates Go/No-Go Project Risk Rating based on detected risks
    """
    for risk in risks:
        if "High number" in risk or "No README" in risk:
            return "Project Risk Rating: No-Go | Significant technical risks detected."
    return "Project Risk Rating: Go | Project looks ready."