    +-----------------------------+
    |  one_bit_video_ditherer.py  |
    +-----------------------------+
  +----------------------------------+
  |    one_bit_frames_ditherer.py    |
  +----------------------------------+
+-------------------------------------+
|      one_bit_image_ditherer.py      |
+-------------------------------------+


**one_bit_video_ditherer.py**
Runs in main()

CLI > python one_bit_video_ditherer.py <input_video_path> <output_video_name> [pixelation_factor] [random_factor] [divergence_factor] [divergence_point]

**one_bit_video_ditherer.py**
process_frame_folder(folder_name, output_folder_name, 
                      pixelation_factor, random_factor, 
                      divergence_factor, divergence_point)

CLI > python one_bit_video_ditherer.py <input_folder_name> <output_folder_name> [pixelation_factor] [random_factor] [divergence_factor] [divergence_point]

**one_bit_image_ditherer.py**
*For videos*
process_frame(image
                pixelation_factor, random_factor, 
                divergence_factor, divergence_point)

*For single images*
CLI > python 1_bit_image_ditherer.py <input_image_path> <output_image_path> [pixelation_factor] [random_factor] [divergence_factor] [divergence_point]

*What happens to the image?*
  1. If it is not already a PIL image it is converted
  2. Turn the image greyscale
  3. Pixelate the image
  4. Convert it to an Numpy array
  5. 