# Oversamples smaller classes using sklearn

import os
from PIL import Image
from sklearn.utils import resample
from pathlib import Path


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        with Image.open(file_path) as img:
            images.append(img.copy())
    return images


def save_images(images, folder):
    for i, img in enumerate(images):
        img.save(os.path.join(folder, f"oversampled_{i}.png"))


def oversample_images(data_dir):
    max_size = 0
    class_folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]

    images_dict = {}
    for folder in class_folders:
        folder_path = os.path.join(data_dir, folder)
        images = load_images_from_folder(folder_path)
        images_dict[folder] = images
        if len(images) > max_size:
            max_size = len(images)

    for folder, images in images_dict.items():
        if len(images) < max_size:
            oversampled_images = resample(images, replace=True, n_samples=max_size, random_state=42)
            save_folder = os.path.join(data_dir, folder)
            Path(save_folder).mkdir(parents=True, exist_ok=True)
            save_images(oversampled_images, save_folder)
            print(f"Saved {len(oversampled_images) - len(images)} oversampled images in {save_folder}")
        else:
            print(f"No oversampling needed for class {folder}")


if __name__ == "__main__":
    data_dir = R'..\data'
    oversample_images(data_dir)
