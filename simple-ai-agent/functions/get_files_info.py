
import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    # Get the absolute and normalized paths for both the full_path and working_directory
    abs_full_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory)

    # Validate that the absolute path to the directory is within the working_directory
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

