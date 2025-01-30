from gendiff.formatters import format_json, format_plain, format_stylish
from gendiff.parse import parse_file


def modified(content):
    if not isinstance(content, dict):
        return content
    
    result = {}
    for key in content.keys():
        result[key] = {
            "status": "unchanged",
            "value": modified(content[key]),
        }

    return result


def build_diff(content1, content2):
    difference = {}

    if not isinstance(content1, dict):
        return content1, modified(content2)
    
    if not isinstance(content2, dict):
        return modified(content1), content2

    keys = content1.keys() | content2.keys()
    for key in keys:
        result = {}
        if key not in content1:
            result["status"] = "added"
            result["value"] = modified(content2[key])
        elif key not in content2:
            result["status"] = "removed"
            result["value"] = modified(content1[key])
        elif content1[key] == content2[key]:
            result["status"] = "unchanged"
            result["value"] = modified(content1[key])
        else:
            result["status"] = "changed"
            result["value"] = build_diff(content1[key], content2[key])
        difference[key] = result
    
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