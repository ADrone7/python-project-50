import json

import yaml


def parse_json(text: str) -> dict:
    return json.loads(text)


def parse_yaml(text: str) -> dict:
    return yaml.load(text, Loader=yaml.FullLoader)


def parse(text: str, format: str) -> dict:
    if format == 'json':
        return parse_json(text)
    elif format in ('yaml', 'yml'):
        return parse_yaml(text)