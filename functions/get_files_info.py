import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    absolute_directory = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_directory, directory))
    first_text: str = f"Result for '{directory}' directory:\n"

    try:
        check_valid = os.path.commonpath([absolute_directory, full_path]) == absolute_directory
    except Exception as e:
        return f"Error: {e}"

    if not check_valid:
        return first_text + f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return first_text + f'    Error: "{directory}" is not a directory'

    list_dir: list[str] = []

    try:
        for item in os.listdir(full_path):
            path_for_complete = os.path.join(full_path, item)
            list_dir.append(f"    - {item}: file_size={os.path.getsize(path_for_complete)} bytes, is_dir={os.path.isdir(path_for_complete)}")

        list_for_return = "\n".join(list_dir)
    except Exception as e:
        return f"Error: {e}"

    if directory == ".":
        return f"Result for current directory:\n" + list_for_return
    return first_text + list_for_return

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
