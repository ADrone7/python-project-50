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


def process_data(report: list, data, key: str, 
                 symbol: str = '', indent: str = '', depth: int = 0) -> None:
    if isinstance(data, dict):
        report.append(f"{indent}{symbol} {key}: " + '{')
        walk_dict(report, data, depth + 1)
    else:
        report.append(f"{indent}{symbol} {key}: {convert(data)}")


def walk_dict(report: list, subdiff: dict, depth: int = 0) -> None:
    indent = (INDENT_COUNT * (depth + 1) - 2) * INDENT
    for key, data in subdiff.items():
        process_data(report, data, key, ' ', indent, depth)
    report.append(depth * INDENT_COUNT * INDENT + '}')


def walk_diff(report: list, subdiff: dict, depth: int = 0) -> None:
    indent = (INDENT_COUNT * (depth + 1) - 2) * INDENT
    for key, data in subdiff.items():
        status = data["status"]
        if status == "added":
            process_data(report, data["value"], key, '+', indent, depth)
            continue
        if status == "removed":
            process_data(report, data["value"], key, '-', indent, depth)
            continue
        if status == "unchanged":
            process_data(report, data["value"], key, ' ', indent, depth)
            continue
        if status == "changed":
            process_data(report, data["old_value"], key, '-', indent, depth)
            process_data(report, data["new_value"], key, '+', indent, depth)
            continue
        if status == "nested change":
            report.append(f"{indent}  {key}: " + '{')
            walk_diff(report, data["value"], depth + 1)
    report.append(depth * INDENT_COUNT * INDENT + '}')


def format_stylish(diff: dict) -> str:
    report = ['{']
    walk_diff(report, diff)
    return SEPARATOR.join(report)