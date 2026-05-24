# Python Basics for AI
def status(marks):
    return "Excellent" if marks >= 75 else "Pass" if marks >= 40 else "Needs Practice"
marks = [78,56,33,91]
for m in marks: print(m, status(m))
print("Average:", sum(marks)/len(marks))
