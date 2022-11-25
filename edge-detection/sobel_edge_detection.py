import numpy as np
from PIL import Image

# load image
image = Image.open("../output/gray_max_pool.jpeg")
data = np.asarray(image.convert("L"))

# initialize a temporary array with size of data but no 3rd RGB dimension
edgeDetected = np.zeros(shape=(data.shape[0], data.shape[1]), dtype=int)

# horizontal operator
hOperator = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# vertical operator
vOperator = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

# apply convolution
for i in range(edgeDetected.shape[0] - 3):
    for j in range(edgeDetected.shape[1] - 3):
        
        # select 3x3 pixel section from image
        imageSection = data[np.ix_(np.arange(3) + i, np.arange(3) + j)]

        # vertical edge
        vEdges = np.multiply(imageSection, vOperator)

        # horizontal edge
        hEdges = np.multiply(imageSection, hOperator)

        # find Euclidean distance
        edgeDetected[i][j] = int(
            (np.sqrt((np.sum(vEdges)) ** 2 + (np.sum(hEdges)) ** 2) / 9)
        )

# save image
im = Image.fromarray(edgeDetected.astype(np.uint8))
im.save("../output/edge.jpeg")
