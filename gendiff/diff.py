from gendiff.parse import parse_file

INDENT = "  "
SEPARATOR = '\n'
STATUS_TO_SYMBOLS = {
    "added": '+',
    "removed": '-',
    "changed": "-+",
    "unchanged": ' ',
}


def modified(content):
    if not isinstance(content, dict):
        return content
    
    result = {}
    for key in content.keys():
        result[key] = {
            "status": "unchanged",
            "values": modified(content[key]),
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
            result["values"] = modified(content2[key])
        elif key not in content2:
            result["status"] = "removed"
            result["values"] = modified(content1[key])
        elif content1[key] == content2[key]:
            result["status"] = "unchanged"
            result["values"] = modified(content1[key])
        else:
            result["status"] = "changed"
            result["values"] = build_diff(content1[key], content2[key])
        difference[key] = result
    
    return difference


def stylish(difference, depth=0):
    if not isinstance(difference, dict):
        if isinstance(difference, bool):
            difference = str(difference).lower()
        elif difference is None:
            difference = 'null'
        return difference

    indent = INDENT * (2 * depth + 1)
    report = ['{']
    for key in sorted(difference.keys()):
        entry = difference[key]
        status = entry["status"]
        match status:
            case "added":
                value = stylish(entry["values"], depth + 1)
                report += [f"{indent}+ {key}: {value}"]
            case "removed":
                value = stylish(entry["values"], depth + 1)
                report += [f"{indent}- {key}: {value}"]
            case "changed":
                if isinstance(entry["values"], dict):
                    value = stylish(entry["values"], depth + 1)
                    report += [f"{indent}  {key}: {value}"]
                else:
                    old_value, new_value = entry["values"]
                    old_value = stylish(old_value, depth + 1)
                    new_value = stylish(new_value, depth + 1)
                    report += [f"{indent}- {key}: {old_value}"]
                    report += [f"{indent}+ {key}: {new_value}"]
            case "unchanged":
                value = stylish(entry["values"], depth + 1)
                report += [f"{indent}  {key}: {value}"]
    report.append(f"{INDENT * (2 * depth)}" + '}')

    return SEPARATOR.join(report)


def generate_diff(file_path1: str, file_path2: str,
                  format_name: str = 'stylish') -> str:
    content1 = parse_file(file_path1)
    content2 = parse_file(file_path2)

    diff = build_diff(content1, content2)
    match format_name:
        case 'stylish':
            result = stylish(diff)
        case _:
            result = stylish(diff)
    return result