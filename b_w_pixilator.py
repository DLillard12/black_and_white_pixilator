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

img = Image.open("input\\tonysoprano.jpg")
img = img.convert(mode='L') # converting to greyscale

# converting to a numpy array so we can set the pixel color.
arr = np.array(img)

# Performing operations
pixelated = pixelate(12,img)  # Higher is more pixelated
pixelated_random = add_random_pixels(pixelated,1024) # lower is more random pixels
pixelated_binary_random = binary_threshold(pixelated_random)


pixelated_binary_random.save(fp='output\\tonysoprano.png')