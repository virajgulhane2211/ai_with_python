# Types of AI
def ai_type(example):
    e = example.lower()
    if "all tasks" in e: return "General AI"
    if "beyond human" in e: return "Super AI"
    return "Narrow AI"
for x in ["Face unlock", "AI for all tasks", "Beyond human AI"]:
    print(x, "=>", ai_type(x))
