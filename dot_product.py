import numpy as np

inputs = [1, 2, 3, 2.5]

weights = [[0.2,0.8,-0.5, 1.0],
		   [0.5,-0.91,0.26, -0.5],
		   [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

#dot product is just for each array in weights multiply by inputs
#code below is the dot product array result plus the biases
output = np.dot(weights, inputs) + biases

print(output)