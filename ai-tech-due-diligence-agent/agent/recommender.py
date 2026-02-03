def make_recommendation(risks):
    """
    Generate Go / No-Go recommendation based on risks.
    """
    for risk in risks:
        if "High number" in risk or "No README" in risk:
            return "No-Go: Project has significant technical risks."
    return "Go: Project looks ready."