# generate image classes summary
import os


def count_files_in_subdirectories(start_directory, output_file):
    # Check if the provided path is a directory
    if not os.path.isdir(start_directory):
        print("The provided path is not a directory.")
        return

    # Traverse through all files and subdirectories in the provided path
    directories = [d for d in os.listdir(start_directory) if os.path.isdir(os.path.join(start_directory, d))]
    whole_dir_count = 0
    # Open a file to write the summary
    with open(output_file, 'w') as file:
        # Iterate through subdirectories and count files in each
        for directory in directories:
            subdirectory_path = os.path.join(start_directory, directory)
            file_count = len(
                [f for f in os.listdir(subdirectory_path) if os.path.isfile(os.path.join(subdirectory_path, f))])
            file.write(f"Number of files in directory {directory}: {file_count}\n")
            whole_dir_count += file_count
        file.write(f"Number of files: {whole_dir_count}\n")

    print(f"Summary has been saved to '{output_file}'.")


directory_path = R'..\data'

output_file = 'files_summary.txt'

count_files_in_subdirectories(directory_path, output_file)
