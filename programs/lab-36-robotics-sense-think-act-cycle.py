# Robotics Sense-Think-Act Cycle
def robot(distance_cm, left_clear, right_clear):
    if distance_cm > 30: return "Move forward"
    if left_clear: return "Turn left"
    if right_clear: return "Turn right"
    return "Stop"
print(robot(15, False, True))
