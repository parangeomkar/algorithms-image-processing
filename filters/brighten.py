import numpy as np
from PIL import Image

# load image
image = Image.open("../output/edge.jpeg")
data = np.asarray(image)

# initialize a temporary array with size of data but no 3rd RGB dimension
brightenedArray = np.zeros(shape=(data.shape[0], data.shape[1]), dtype=int)

x = 0
for row in data:

    y = 0
    for pixel in row:
        
        # multiply grayscale pixel by brightening factor
        gray = min(255, int(pixel * 3))

        brightenedArray[x][y] = gray
        y += 1
    x += 1

# save image
im = Image.fromarray(brightenedArray.astype(np.uint8))
im.save("../output/brightened_edge.jpeg")
