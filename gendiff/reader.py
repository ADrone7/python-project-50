def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read()
    return content


def get_format(file_path: str) -> str:
    dot_position = file_path.rindex('.')
    format = file_path[dot_position + 1:]
    return format