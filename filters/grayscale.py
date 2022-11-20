import pandas as pd
import numpy as np
from PIL import Image

# load image
image = Image.open("../data/image.jpg")
data = np.asarray(image)

# initialize a temporary array with size of data but no 3rd RGB dimension
grayscaleArray = np.zeros(shape=(data.shape[0], data.shape[1]), dtype=int)

x = 0
for row in data:

    y = 0
    for pixel in row:

        # max pool from RGB values
        gray = int(np.max(pixel))

        ## avg pool from RGB values
        # gray = int(np.mean(pixel))

        grayscaleArray[x][y] = gray
        y += 1
    x += 1

# save image
im = Image.fromarray(grayscaleArray.astype(np.uint8))
im.save("../output/gray_max_pool.jpeg")
