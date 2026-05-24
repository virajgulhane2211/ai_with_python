# Classification Basics
def classify(marks, attendance):
    return "Pass" if marks >= 40 and attendance >= 60 else "Needs Support"
for s in [(72,80),(38,90),(58,45)]:
    print(s, "=>", classify(*s))
