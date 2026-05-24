# CNN Convolution Filter
image = [[10,10,200],[10,10,200],[10,10,200]]
filter_ = [[1,0,-1],[1,0,-1],[1,0,-1]]
response = sum(image[i][j]*filter_[i][j] for i in range(3) for j in range(3))
print("Convolution response:", response)
