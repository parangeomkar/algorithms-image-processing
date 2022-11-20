import pandas as pd
import numpy as np
from PIL import Image

# load image
image = Image.open("../output/gray_max_pool.jpeg")
data = np.asarray(image)

# initialize a temporary array with size of data but no 3rd RGB dimension
edgeDetected = np.zeros(shape=(data.shape[0], data.shape[1]), dtype=int)

# apply convolution
for i in range(edgeDetected.shape[0] - 3):
    for j in range(edgeDetected.shape[1] - 3):

        # horizontal edge
        a11 = int(np.mean(data[i][j])) * 1
        a12 = int(np.mean(data[i][j + 1])) * 2
        a13 = int(np.mean(data[i][j + 2])) * 1

        a21 = int(np.mean(data[i + 1][j])) * 0
        a22 = int(np.mean(data[i + 1][j + 1])) * 0
        a23 = int(np.mean(data[i + 1][j + 2])) * 0

        a31 = int(np.mean(data[i + 2][j])) * -1
        a32 = int(np.mean(data[i + 2][j + 1])) * -2
        a33 = int(np.mean(data[i + 2][j + 2])) * -1

        # vertical edge
        b11 = int(np.mean(data[i][j])) * 1
        b12 = int(np.mean(data[i][j + 1])) * 0
        b13 = int(np.mean(data[i][j + 2])) * -1

        b21 = int(np.mean(data[i + 1][j])) * 2
        b22 = int(np.mean(data[i + 1][j + 1])) * 0
        b23 = int(np.mean(data[i + 1][j + 2])) * -2

        b31 = int(np.mean(data[i + 2][j])) * 1
        b32 = int(np.mean(data[i + 2][j + 1])) * 0
        b33 = int(np.mean(data[i + 2][j + 2])) * -1

        # find Euclidean distance
        edgeDetected[i][j] = int(
            (
                np.sqrt(
                    (a11 + a12 + a13 + a21 + a22 + a23 + a31 + a32 + a33) ** 2
                    + (b11 + b12 + b13 + b21 + b22 + b23 + b31 + b32 + b33) ** 2
                )
                / 9
            )
        )
        
# save image
im = Image.fromarray(edgeDetected.astype(np.uint8))
im.save("../output/edge.jpeg")
