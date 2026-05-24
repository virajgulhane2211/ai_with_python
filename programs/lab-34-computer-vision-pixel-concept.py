# Computer Vision Pixel Concept
image = [[0,40,80],[120,160,200],[220,240,255]]
pixels = [p for row in image for p in row]
avg = sum(pixels)/len(pixels)
print("Average brightness:", round(avg,2))
print("Image type:", "Bright" if avg > 127 else "Dark")
