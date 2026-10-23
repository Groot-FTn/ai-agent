import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    absolute_directory = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_directory, directory))
    check_valid = os.path.commonpath([absolute_directory, full_path]) == absolute_directory
    if check_valid == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'
    elif os.path.isdir(directory) == True:
        return f'Success: "{directory}" is within the working directory'
