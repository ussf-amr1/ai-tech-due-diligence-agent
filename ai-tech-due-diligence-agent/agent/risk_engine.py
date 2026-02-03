def assess_risks(file_report):
    """
    Assess technical risks based on file report.
    """
    risks = []

    if file_report.get('py', 0) > 50:
        risks.append("High number of Python files – potential complexity risk.")

    if file_report.get('md', 0) == 0:
        risks.append("No README found – lack of documentation.")

    if 'js' in file_report and file_report.get('py', 0) == 0:
        risks.append("No Python backend detected – might lack server logic.")

    if not risks:
        risks.append("No major risks detected.")

    return risks