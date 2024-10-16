# Removes all images generated in data_preprocessing and oversampler scripts
import os


def delete_rotated_images(directory_path):
    if not os.path.isdir(directory_path):
        print("The provided path is not a directory.")
        return

    deleted_count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if 'rotated' in file.lower() or 'flip' or 'oversampled' in file.lower():
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"Error while trying to delete {file_path}: {e}")

    # Print out the result
    if deleted_count > 0:
        print(f"Total deleted files: {deleted_count}")
    else:
        print("No 'rotated' files found to delete.")


# Example usage
directory_path = R'..\data'
delete_rotated_images(directory_path)
