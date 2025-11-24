# Daniel Lillard
# 2025.05.19
# This is a small project to pixilate an image and turn in b & w
# inspired by: https://www.youtube.com/watch?v=nvR8__cVifI

# ---------------
#   Imports
# ---------------
import numpy as np
from PIL import Image
import random

# --------------
#   Constants
# --------------

b = 255
w = 0
patterns = np.array([
    [[w,w,w],[w,w,w],[w,w,w]],        # bucket 0
    [[w,w,w],[w,b,w],[w,w,w]],      # bucket 1
    [[b,w,b],[w,w,w],[b,w,b]],# bucket 2
    [[w,b,w],[b,b,b],[w,b,w]], # bucket 3
    [[b,b,b],[b,w,b],[b,b,b]], # bucket 4
    [[b,b,b],[b,b,b],[b,b,b]] # bucket 5
], dtype=np.uint8)

# patterns = np.array([
#     [[w,w,w]],        # bucket 0
#     [[w,w,w]],      # bucket 1
#     [[b,w,b]],# bucket 2
#     [[w,b,w]], # bucket 3
#     [[b,b,b]], # bucket 4
#     [[b,b,b]] # bucket 5
# ], dtype=np.uint8)

# --------------
# Functions
# --------------

def bucket_index(img):
    bins = np.array([43, 85, 128, 170, 213, 256])
    return np.digitize(img, bins)     # shape: (H, W)

def pixelate(pixelation_factor: int , img: Image):
    tiny = img.resize(size=[int(img.width/pixelation_factor),int(img.height/pixelation_factor)])
    return tiny


def binary_threshold(img: Image):
    pixels = img.load()  # Gives access to pixel data
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > 70: # for now just setting threshold to halfway.
                pixels[x,y] = 255
            else:
                pixels[x,y] = 0
    return img

def add_random_pixels(img_array: np.array, random_factor: int):
    # Generate the random pixel coordinates
    rng = np.random.default_rng()
    H, W = img_array.shape
    num_random_pixels = int(random_factor**1.5)
    random_pixels = rng.integers(0, [H, W], size=(num_random_pixels,2))
    unique = np.unique(random_pixels, axis=0)
    
    # separate into x and y coords
    x_coords = unique[:, 0]
    y_coords = unique[:, 1]

    # now set those pixels to random black or white
    img_array[x_coords, y_coords] = np.random.choice([0, 255], size=unique.shape[0])

    return img_array


def expand_pixels(img_array):
    img_array = img_array.astype(np.uint8)

    idx = bucket_index(img_array)        # (H, W)
    mapped = patterns[idx]               # (H, W, 3, 3)
    H, W = img_array.shape

    mapped = mapped.transpose(0, 2, 1, 3)

    # now flatten the first two and last two dimensions
    out = mapped.reshape(H*3, W*3).astype(np.uint8)

    return out

# --------------
# Main Code
# --------------

img = Image.open("input\\tony_soprano.jpg")
img = img.convert(mode='L') # converting to greyscale

# converting to a numpy array.
arr = np.array(img)

# # Performing operations
# pixelated = pixelate(4,img)  # Higher is more pixelated
# pixelated_random = add_random_pixels(pixelated,4096)

# expanded_pixels = expand_pixels(np.array(pixelated))


# print(np.array(pixelated).shape, np.array(pixelated).dtype)   # should be (H/4, W/4) uint8
# print(expanded_pixels.shape, expanded_pixels.dtype)   # should be (H*3, W*3) uint8


arr_random = add_random_pixels(arr, 4444)
expanded_pixels = expand_pixels(arr)
expanded_pixels = Image.fromarray(np.uint8(expanded_pixels))

expanded_pixels.save(fp='output\\tony_soprano.jpg')
