import json

import yaml


def read_json(file_path: str) -> dict:
    with open(file_path) as file:
        parsed = json.load(file)
    return parsed


def read_yaml(file_path: str) -> dict:
    with open(file_path) as file:
        parsed = yaml.load(file, Loader=yaml.FullLoader)
    return parsed
