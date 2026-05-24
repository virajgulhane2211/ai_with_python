# ML vs Deep Learning Decision
def choose(data_type, size):
    return "Deep Learning" if data_type in ["image","text","audio"] and size == "large" else "Machine Learning"
print(choose("image", "large"))
print(choose("table", "small"))
