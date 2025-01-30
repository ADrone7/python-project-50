import json


def format_json(diff, path=None):
    result = json.dumps(diff, sort_keys=True, indent=4)
    return result