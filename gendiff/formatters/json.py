INDENT = ' '
INDENT_COUNT = 4
SEPARATOR = '\n'


def convert(value) -> str:
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f'"{value}"'
    else:
        value = str(value)
    return value


def walk_list(report: list, subdiff: list | tuple, depth: int = 0) -> None:
    indent = (depth + 1) * INDENT_COUNT * INDENT
    for i, data in enumerate(subdiff):
        if isinstance(data, dict):
            report.append(f'{indent}' + '{')
            walk_dict(report, data, depth + 1)
        elif isinstance(data, (list, tuple)):
            report.append(f'{indent}' + '[')
            walk_list(report, data, depth + 1)
        else:
            report.append(f'{indent}{convert(data)}')
        if i == len(subdiff) - 1:
            continue
        report[-1] += ','
    report.append(depth * INDENT_COUNT * INDENT + ']')


def walk_dict(report: list, subdiff: dict, depth: int = 0) -> None:
    indent = (depth + 1) * INDENT_COUNT * INDENT
    for i, (key, data) in enumerate(sorted(subdiff.items())):
        if isinstance(data, dict):
            report.append(f'{indent}"{key}": ' + '{')
            walk_dict(report, data, depth + 1)
        elif isinstance(data, (list, tuple)):
            report.append(f'{indent}"{key}": ' + '[')
            walk_list(report, data, depth + 1)
        else:
            report.append(f'{indent}"{key}": {convert(data)}')
        if i == len(subdiff) - 1:
            continue
        report[-1] += ','
    report.append(depth * INDENT_COUNT * INDENT + '}')


def format_json(diff: dict) -> str:
    report = ['{']
    walk_dict(report, diff, 0)
    return SEPARATOR.join(report)