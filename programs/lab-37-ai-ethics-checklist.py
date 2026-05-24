# AI Ethics Checklist
checklist = {"Privacy":True, "Bias test":True, "Explainable":False, "Human review":True}
score = sum(checklist.values())
for item, ok in checklist.items(): print(item, "Yes" if ok else "No")
print("Score:", score, "/", len(checklist))
