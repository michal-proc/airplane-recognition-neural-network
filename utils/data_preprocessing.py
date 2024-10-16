# generates additional data for model training by rotating and flipping images
import os
from PIL import Image


def rotate_and_flip_images_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        print("The provided path is not a directory.")
        return

    image_counter = 0
    successful_operations = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        # Rotate the image
                        rotated_img = img.rotate(180)
                        rotated_img.save(f"{os.path.splitext(image_path)[0]}_rotated_180.jpg")

                        # Flip the image horizontally
                        h_flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                        h_flip_img.save(f"{os.path.splitext(image_path)[0]}_hflip.jpg")

                        # Flip the image horizontally and vertically
                        hv_flip_img = h_flip_img.transpose(Image.FLIP_TOP_BOTTOM)
                        hv_flip_img.save(f"{os.path.splitext(image_path)[0]}_hvflip.jpg")

                        successful_operations += 1
                        if successful_operations % 100 == 0:
                            print(f"Processed {successful_operations} images successfully.")
                except Exception as e:
                    print(f"An error occurred while processing the file {file}: {e}")
                image_counter += 1

    print(f"Total images processed: {image_counter}")
    print(f"Total successful operations: {successful_operations}")


directory_path = R'..\data'
rotate_and_flip_images_in_directory(directory_path)
