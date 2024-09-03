# Run 'python3 JPG_to_PNG_converter.py Pokedex/ new/'
# Open img folder, convert images to PNG and save to a new folder

from PIL import Image
import sys
import os

# Grab the 1st and 2nd arg from cmdline (folder name and new folder name)
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if new folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through img folder, convert to PNG and then save to new folder
for filename in os.listdir(img_folder):
    image = Image.open(f'{img_folder}{filename}')
    clean_name = os.path.splitext(filename)[0] # returns a tuple ("filename", "extension (i.e 'png'))
    image.save(f'{output_folder}{clean_name}.png', 'png')