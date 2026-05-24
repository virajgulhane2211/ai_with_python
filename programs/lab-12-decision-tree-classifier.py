# Decision Tree Classifier
def placement(cgpa, skills, projects):
    if cgpa < 7: return "Improve CGPA"
    if skills < 6: return "Improve programming"
    if projects < 1: return "Do mini project"
    return "Placement Ready"
print(placement(8.2,7,2))
