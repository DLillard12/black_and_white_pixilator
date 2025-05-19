# Danny Lillard
# 2025.05.19
# I am having issues with b_w_pixelator, I cannot seem to get pixelation down, for that I am making a
# small test script here to ascertain the issue.

# First thought: Pixelation must be peformed before the randomness and b & w operations
# this likely will not help, but may make the end product better.

# Second thought: The image of the cairn is too complex.

import numpy as np
from PIL import Image

img = Image.open("input\\woman.jpg")
# img = img.convert(mode='L') # converting to greyscale

resize_factor = 1000
# tiny = img.resize(size=[int(arr.shape[1]/resize_factor),int(arr.shape[0]/resize_factor)])

#tiny = img.resize((int(img.width / 2),int(img.height / 2)))

tiny = img.resize((10,10),resample=Image.BOX)

tiny.save(fp='output\\tiny_woman.jpg')

img = tiny.resize(img.size,Image.BOX)   # resizing the smaller image to the original size

img.save(fp='output\\pixelated_woman.jpg')