# Removes all files which are too small
import os
from PIL import Image


def is_image_small(filepath):
    with Image.open(filepath) as img:
        return img.width < 128 or img.height < 128


def remove_small_images(directory):
    counter = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                try:
                    if is_image_small(file_path):
                        os.remove(file_path)
                        counter += 1
                except Exception as e:
                    print(f'Error removing {file_path}: {e}')
    print(counter)


directory_to_search = R'..\data'

remove_small_images(directory_to_search)
