# Daniel Lillard
# 2025.05.19
# This is a small project to pixilate an image and turn in b & w
# inspired by: https://www.youtube.com/watch?v=nvR8__cVifI

# ---------------
#   Imports
# ---------------
import numpy as np
from PIL import Image
import os

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

# this function takes a value, and moves it from its position away from 128
def pixel_divergence(img_arr: np.array, divergence_factor: float):
    # center the values around 0
    centered = img_arr - 128.0
    # scale by divergence factor
    scaled = centered * divergence_factor
    # re-center around 128
    re_centered = scaled + 128.0
    # clip to valid range
    clipped = np.clip(re_centered, 0, 255)
    return clipped.astype(np.uint8)
    

def add_random_pixels(img_array: np.array, random_factor: int):
    # Generate the random pixel coordinates
    rng = np.random.default_rng()
    H, W = img_array.shape
    num_random_pixels = int(random_factor**1.5)
    random_pixels = rng.integers(0, [H, W], size=(num_random_pixels,2))
    
    # separate into x and y coords
    x_coords = random_pixels[:, 0]
    y_coords = random_pixels[:, 1]

    # now set those pixels to random black or white
    img_array[x_coords, y_coords] = np.random.choice([0, 255], size=random_pixels.shape[0])

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

# img = Image.open("input\\sam_elliot_big_lebowski.jpg")
# img = img.convert(mode='L') # converting to greyscale

# # Performing operations on image object
# img_pixelated = pixelate(2,img)  # Higher is more pixelated

# # converting to a numpy array.
# # Operations from now on expect a numpy array.
# arr = np.array(img_pixelated)

# arr = pixel_divergence(arr, 20)

# arr_random = add_random_pixels(arr, 44)
# arr_dithered = expand_pixels(arr)
# final_image = Image.fromarray(np.uint8(arr_dithered))

# final_image.save(fp='output\\sam_elliot_big_lebowski.jpg')


# moving on to videos.

input_video_path = "input\\knights_fighting_frames\\"
output_video_path = "output\\knights_fighting_frames\\"

pixelation_factor = 2
divergence_factor = 10
random_factor = 8

for fname in sorted(os.listdir(input_video_path)):
    # every 60 frames have a set chance parameters walk by one
    frame_number = int(fname.split('_')[1].split('.')[0])
    if frame_number % 60 == 0:
        if np.random.rand() < 0.1:
            step = np.random.choice([-3,3])
            pixelation_factor = max(1, pixelation_factor + step)
        if np.random.rand() < 0.1:
            step = np.random.choice([-3,3])
            divergence_factor = max(1, divergence_factor + step)
        if np.random.rand() < 0.1:
            step = np.random.choice([-3,3])
            random_factor = max(1, random_factor + step)
        print(f"New parameters at frame {fname}: pixelation_factor={pixelation_factor}, divergence_factor={divergence_factor}, random_factor={random_factor}")

    if not fname.endswith('.png'):
        continue
    
    path = os.path.join(input_video_path, fname)
    img = Image.open(path).convert('L')

    # Performing operations on image object
    img_pixelated = pixelate(2,img)  # Higher is more pixelated

    # converting to a numpy array.
    # Operations from now on expect a numpy array.
    arr = np.array(img_pixelated)

    arr = pixel_divergence(arr, 10)

    arr_random = add_random_pixels(arr, 8)
    arr_dithered = expand_pixels(arr)
    final_image = Image.fromarray(np.uint8(arr_dithered))
   
    final_image.save(os.path.join(output_video_path, fname))