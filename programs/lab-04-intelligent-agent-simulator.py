# Intelligent Agent Simulator
def agent(battery, obstacle_cm, task_done):
    if task_done: return "Stop"
    if battery < 25: return "Charge"
    if obstacle_cm < 20: return "Turn"
    return "Move forward"
print(agent(60, 12, False))
