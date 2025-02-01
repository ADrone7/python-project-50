INDENT = ' '
INDENT_COUNT = 4
SEPARATOR = '\n'


def convert(value) -> str:
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    else:
        value = str(value)
    return value


def format_stylish(diff: dict) -> str:
    report = ['{']

    def walk_dict(subdiff: dict, depth: int = 0) -> None:
        indent = (INDENT_COUNT * (depth + 1) - 2) * INDENT
        for key, data in subdiff.items():
            if isinstance(data, dict):
                report.append(f"{indent}  {key}: " + '{')
                walk_dict(data, depth + 1)
                continue
            report.append(f"{indent}  {key}: {convert(data)}")
        report.append(depth * INDENT_COUNT * INDENT + '}')

    def walk_diff(subdiff: dict, depth: int = 0) -> None:
        indent = (INDENT_COUNT * (depth + 1) - 2) * INDENT
        for key, data in subdiff.items():
            status = data["status"]
            if status == "added":
                if isinstance(data["value"], dict):
                    report.append(f"{indent}+ {key}: " + '{')
                    walk_dict(data["value"], depth + 1)
                else:
                    report.append(f"{indent}+ {key}: {convert(data["value"])}")
                continue
            if status == "removed":
                if isinstance(data["value"], dict):
                    report.append(f"{indent}- {key}: " + '{')
                    walk_dict(data["value"], depth + 1)
                else:
                    report.append(f"{indent}- {key}: {convert(data["value"])}")
                continue
            if status == "unchanged":
                if isinstance(data["value"], dict):
                    report.append(f"{indent}  {key}: " + '{')
                    walk_dict(data["value"], depth + 1)
                else:
                    report.append(f"{indent}  {key}: {convert(data["value"])}")
                continue
            if status == "changed":
                old = data["old_value"]
                new = data["new_value"]
                if isinstance(old, dict):
                    report.append(f"{indent}- {key}: " + '{')
                    walk_dict(old, depth + 1)
                else:
                    report.append(f"{indent}- {key}: {convert(old)}")
                if isinstance(new, dict):
                    report.append(f"{indent}+ {key}: " + '{')
                    walk_dict(new, depth + 1)
                else:
                    report.append(f"{indent}+ {key}: {convert(new)}")
                continue
            if status == "nested change":
                report.append(f"{indent}  {key}: " + '{')
                walk_diff(data["value"], depth + 1)
        report.append(depth * INDENT_COUNT * INDENT + '}')

    walk_diff(diff)
    return SEPARATOR.join(report)