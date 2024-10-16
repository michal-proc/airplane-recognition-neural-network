# Generates all class names
import os


def generate_directory_list(start_directory):
    if not os.path.isdir(start_directory):
        print("The provided path is not a directory.")
        return

    directories = [d for d in os.listdir(start_directory) if os.path.isdir(os.path.join(start_directory, d))]

    with open('subdirectory_names.txt', 'w') as file:
        for i, directory in enumerate(directories, start=1):
            file.write(f"{i} {directory}\n")

    print("Created 'subdirectory_names.txt' file with the names of subdirectories.")


directory_path = R'..\data'

generate_directory_list(directory_path)
