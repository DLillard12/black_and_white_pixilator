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

def add_random_pixels(img: Image, random_factor: int):
    width, height = img.size
    
    pixels = img.load()  # Gives access to pixel data
    num_rand_pixels = random.randint(0,arr.shape[0] * arr.shape[1] // random_factor)
    for _ in range(num_rand_pixels):
        rand_x = random.randint(0,width-1)
        rand_y = random.randint(0,height-1)
        pixels[rand_x, rand_y] = random.randint(0,255)
    print('Number of random pixels: ', num_rand_pixels)
    return img

def expand_pixels(img_array):
    img_array = img_array.astype(np.uint8)

    idx = bucket_index(img_array)        # (H, W)
    mapped = patterns[idx]               # (H, W, 3, 3)
    H, W = img_array.shape

    # reorder axes so blocks tile correctly:
    # original:  H, W, bh, bw
    # want:      H, bh, W, bw
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
# arr = np.array(img)

# # Performing operations
# pixelated = pixelate(4,img)  # Higher is more pixelated
# pixelated_random = add_random_pixels(pixelated,4096) # lower is more random pixels

# expanded_pixels = expand_pixels(np.array(pixelated))


# print(np.array(pixelated).shape, np.array(pixelated).dtype)   # should be (H/4, W/4) uint8
# print(expanded_pixels.shape, expanded_pixels.dtype)   # should be (H*3, W*3) uint8

expanded_pixels = expand_pixels(img_array=np.array(img))
expanded_pixels = Image.fromarray(np.uint8(expanded_pixels))


print('expanded_pixels size: ', expanded_pixels.size)

print('img size: ', img.size)

expanded_pixels.save(fp='output\\tony_soprano.jpg')
