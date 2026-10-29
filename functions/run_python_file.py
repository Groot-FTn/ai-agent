import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    absolute_directory = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_directory, file_path))
    output: list[str] = []

    if os.path.commonpath([absolute_directory, full_path]) != absolute_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    elif not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python", full_path]
        if args != None:
            command.extend(args)

        result = subprocess.run(command, cwd=absolute_directory, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a python file with optional arguments and return, if any, an output",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Name of the python file thats the user is trying to run",
                "args": {
                    "type": "array",
                    "items": "string",
                    "description": "Array whose items are string, serves to define more arguments to run the file",
                },
                },
            },
        },
    },
}
