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
import sys # for command line args

from one_bit_image_ditherer import (process_frame)


# --------------
#   Constants
# --------------

# --------------
# Functions
# --------------

# logic is held in one_bit_image_ditherer.py to process each frame

def process_frame_folder(video_name: str, processed_video_name: str, pixelation_factor: int, random_factor: int, divergence_factor: float, divergence_point: float):
    input_video_path = "input\\" + video_name + "_frames\\" 
    output_video_path = "output\\" + processed_video_name + "_frames\\"

    if not os.path.exists(output_video_path):
        os.makedirs(output_video_path)

    for fname in sorted(os.listdir(input_video_path)):

        if not fname.endswith('.png'):
            continue
        
        path = os.path.join(input_video_path, fname)
        img = Image.open(path).convert('L')

        final_image = process_frame(img, pixelation_factor, random_factor, divergence_factor, divergence_point)
    
        final_image.save(os.path.join(output_video_path, fname))

# --------------
# Main Code
# --------------


def main():
    #"input\\*_frames\\" Just need to put the frames name here
    input_video_path = "input\\" + sys.argv[1] + "_frames\\" 
    output_video_path = "output\\" + sys.argv[2] + "_frames\\"

    if not os.path.exists(output_video_path):
        os.makedirs(output_video_path)

    # default parameters
    pixelation_factor = 12
    random_factor = 8
    divergence_factor = 4
    divergence_point = 128.0

    if len(sys.argv) >= 4:
        pixelation_factor = int(sys.argv[3])
    if len(sys.argv) >= 5:
        random_factor = int(sys.argv[4])
    if len(sys.argv) >= 6:
        divergence_factor = float(sys.argv[5])
    if len(sys.argv) >= 7:
        divergence_point = float(sys.argv[6])
    

    process_frame_folder(sys.argv[1], pixelation_factor, random_factor, divergence_factor, divergence_point)

if __name__ == "__main__":
    main()