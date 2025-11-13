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
# Functions
# --------------

# Defining buckets for pixel expansion
# Just making 4 for now.
def pixel_buckets(pixel_value : int):
    if pixel_value < 63:
        return np.array([
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]
], dtype=float)
    elif pixel_value < 126:
        return np.array([
                        [255, 0, 255],
                        [0, 0, 0],
                        [255, 0, 255]
], dtype=float)
    elif pixel_value < 189:
        return np.array([
                        [0, 255, 0],
                        [255, 255, 255],
                        [0, 255, 0]
], dtype=float)
    elif pixel_value < 256:
        return np.array([
                        [255, 255, 255],
                        [255, 255, 255],
                        [255, 255, 255]
], dtype=float)
    else:
        return 255

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

def expand_pixels(img_array: np.ndarray):
    expanded = np.zeros((img_array.shape[0]*3, img_array.shape[1]*3))
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            expanded[i*3:(i+1)*3, j*3:(j+1)*3] = pixel_buckets(img_array[i][j])
    return expanded

# --------------
# Main Code
# --------------

img = Image.open("input\\sam_elliot_big_lebowski.jpg")
img = img.convert(mode='L') # converting to greyscale

# converting to a numpy array so we can set the pixel color.
arr = np.array(img)

# Performing operations
pixelated = pixelate(2,img)  # Higher is more pixelated
pixelated_random = add_random_pixels(pixelated,2056) # lower is more random pixels
# pixelated_binary_random = binary_threshold(pixelated_random)

expanded_pixels = expand_pixels(np.array(pixelated))
expanded_pixels = Image.fromarray(np.uint8(expanded_pixels))


expanded_pixels.save(fp='output\\sam_elliot_big_lebowski.png')
