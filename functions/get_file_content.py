import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:

    absolute_directory = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_directory, file_path))

    if os.path.commonpath([absolute_directory, full_path]) != absolute_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get the content of files in a specified directory relative to the working directory, providing the first 10000 characters.",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                "type": "string",
                "description": "Name of the file thats the user is trying to read it's content",
                },
            },
        },
    },
}
