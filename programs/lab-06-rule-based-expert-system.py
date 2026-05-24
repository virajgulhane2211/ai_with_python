# Rule-Based Expert System: Computer Troubleshooting
def troubleshoot(power, beep, display):
    if not power: return "Check power cable"
    if beep and not display: return "Check RAM or monitor"
    if display: return "System working"
    return "General inspection required"
print(troubleshoot(True, True, False))
