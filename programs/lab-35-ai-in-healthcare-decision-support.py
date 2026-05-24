# AI in Healthcare Decision Support (educational only)
def priority(risk, report_available, human_review):
    if not human_review: return "Human expert review required"
    if risk >= 0.70 and report_available: return "High priority follow-up suggested"
    if risk >= 0.40: return "Moderate priority monitoring suggested"
    return "Routine monitoring suggested"
print(priority(0.72, True, True))
print("Note: learning example only, not a diagnosis.")
