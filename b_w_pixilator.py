# Daniel Lillard
# 2025.05.19
# This is a small project to pixilate an image and turn in b & w
# inspired by: https://www.youtube.com/watch?v=nvR8__cVifI

import numpy as np
from PIL import Image
import random

img = Image.open("input\\woman.jpg")
img = img.convert(mode='L') # converting to greyscale

# converting to a numpy array so we can set the pixel color.
arr = np.array(img)
print(arr.shape)  # (784, 1200, 3) or (784, 1200) for grayscale
print(arr[0])

# setting the random elements.
num_rand_pixels = random.randint(0,int(arr.shape[0] * arr.shape[1] / 4))
print('Number of random pixels: ', num_rand_pixels)

rand_pixel_matrix = []
# randomly choosing where those random pixels should go:
for i in range(num_rand_pixels):
    rand_x = random.randint(0,arr.shape[0]-1)
    rand_y = random.randint(0,arr.shape[1]-1)
    arr[rand_x][rand_y] = random.randint(0,255)



for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        if arr[x][y] > 127: # for now just setting threshold to halfway.
            arr[x][y] = 255
        else:
            arr[x][y] = 0

img = Image.fromarray(arr)

# pixelating, first trying to pixelate after the floor/ceiling function.

resize_factor = 16
tiny = img.resize(size=[int(arr.shape[1]/resize_factor),int(arr.shape[0]/resize_factor)])

pixelated = tiny.resize(img.size,Image.BOX)   # resizing the smaller image to the original size

pixelated.save(fp='output\\pixelated_rand_grey_woman.jpg')