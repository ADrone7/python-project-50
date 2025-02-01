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


def format_json(diff: dict) -> str:
    report = ['{']
    indent_base = INDENT_COUNT * INDENT
        
    def walk_list(subdiff: list | tuple, depth: int = 0) -> None:
        indent = (depth + 1) * indent_base
        for i, data in enumerate(subdiff):
            if isinstance(data, dict):
                report.append(f'{indent}' + '{')
                walk_dict(data, depth + 1)
            elif isinstance(data, (list, tuple)):
                report.append(f'{indent}' + '[')
                walk_list(data, depth + 1)
            else:
                report.append(f'{indent}{convert(data)}')
            if i == len(subdiff) - 1:
                continue
            report[-1] += ','
        report.append(depth * indent_base + ']')

    def walk_dict(subdiff: dict, depth: int = 0) -> None:
        indent = (depth + 1) * indent_base
        for i, (key, data) in enumerate(sorted(subdiff.items())):
            if isinstance(data, dict):
                report.append(f'{indent}"{key}": ' + '{')
                walk_dict(data, depth + 1)
            elif isinstance(data, (list, tuple)):
                report.append(f'{indent}"{key}": ' + '[')
                walk_list(data, depth + 1)
            else:
                report.append(f'{indent}"{key}": {convert(data)}')
            if i == len(subdiff) - 1:
                continue
            report[-1] += ','
        report.append(depth * indent_base + '}')

    walk_dict(diff)
    return SEPARATOR.join(report)