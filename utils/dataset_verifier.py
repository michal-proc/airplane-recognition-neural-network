# Quickly verifies if all images are ok

from PIL import Image
import pathlib

# The path to your dataset
dataset_path = R'/data'
data_dir = pathlib.Path(dataset_path)

# List to hold names of corrupt files
corrupt_files = []

# Loop over each file in the dataset directory and its subdirectories
for image_path in data_dir.glob('**/*'):
    # Make sure it's a file
    if image_path.is_file():
        # Open the image file
        try:
            with Image.open(image_path) as img:
                # Attempt to verify the image. This will not read the whole image,
                # but it will check that it has a valid format.
                img.verify()  # img.verify() is enough if we are just verifying format validity
        except (IOError, SyntaxError) as e:
            print('Bad file:', image_path)  # Print out the names of corrupt files
            corrupt_files.append(image_path)

# Remove corrupt files
for bad_file in corrupt_files:
    print(f"Removing corrupt file: {bad_file}")
    bad_file.unlink()  # This will delete the file

# Print out the result
if corrupt_files:
    print(f"Removed {len(corrupt_files)} corrupt files.")
else:
    print("All files are okay.")
