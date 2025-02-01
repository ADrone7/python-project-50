from gendiff.formatters import format_json, format_plain, format_stylish
from gendiff.parse import parse_file


def build_diff(content1: dict, content2: dict) -> dict:
    difference = {}

    def walk_dicts(data1: dict, data2: dict, parent: dict) -> None:
        keys = data1.keys() | data2.keys()
        for key in sorted(keys):
            result = {}
            if key not in data1:
                result["status"] = "added"
                result["value"] = data2[key]
            elif key not in data2:
                result["status"] = "removed"
                result["value"] = data1[key]
            elif data1[key] == data2[key]:
                result["status"] = "unchanged"
                result["value"] = data1[key]
            elif not isinstance(data1[key], dict) or \
                 not isinstance(data2[key], dict):
                result["status"] = "changed"
                result["old_value"] = data1[key]
                result["new_value"] = data2[key]
            else:
                result["status"] = "nested change"
                result["value"] = {}
                walk_dicts(data1[key], data2[key], result["value"])
            parent[key] = result
    
    walk_dicts(content1, content2, difference)
    return difference


def generate_diff(file_path1: str, file_path2: str,
                  format_name: str = 'stylish') -> str:
    content1 = parse_file(file_path1)
    content2 = parse_file(file_path2)

    diff = build_diff(content1, content2)
    match format_name:
        case 'stylish':
            result = format_stylish(diff)
        case 'plain':
            result = format_plain(diff)
        case 'json':
            result = format_json(diff)
        case _:
            result = format_stylish(diff)
    return result