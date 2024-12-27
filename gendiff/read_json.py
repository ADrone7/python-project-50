import json


def read_json(file_path: str):
    with open(file_path) as file:
        parsed = json.load(file)
    return parsed
