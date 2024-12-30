from gendiff.readers import read_json, read_yaml

FORMATS = {
    'json': read_json,
    'yaml': read_yaml,
    'yml': read_yaml,
}


def parse_file(file_path: str) -> dict:
    position = file_path.rindex('.')
    format = file_path[position + 1:]
    return FORMATS[format](file_path)