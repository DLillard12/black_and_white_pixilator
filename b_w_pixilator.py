# Daniel Lillard
# 2025.05.19
# This is a small project to pixilate an image and turn in b & w
# inspired by: https://www.youtube.com/watch?v=nvR8__cVifI

import numpy as np
from PIL import Image
import random

img = Image.open("input\\cairn.jpg")
img = img.convert(mode='L') # converting to greyscale

# converting to a numpy array so we can set the pixel color.
arr = np.array(img)
print(arr.shape)  # (784, 1200, 3) or (784, 1200) for grayscale
print(arr[0])





for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        if arr[x][y] > 127: # for now just setting threshold to halfway.
            arr[x][y] = 255
        else:
            arr[x][y] = 0

img = Image.fromarray(arr)

img.save(fp='output\\grey_cairn.jpg')