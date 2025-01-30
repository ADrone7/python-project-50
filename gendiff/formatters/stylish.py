INDENT = "  "
SEPARATOR = '\n'
STATUS_TO_SYMBOLS = {
    "added": '+',
    "removed": '-',
    "changed": "-+",
    "unchanged": ' ',
}


def format_stylish(diff, depth=0):
    if not isinstance(diff, dict):
        if isinstance(diff, bool):
            diff = str(diff).lower()
        elif diff is None:
            diff = 'null'
        return diff

    indent = INDENT * (2 * depth + 1)
    report = ['{']
    for key in sorted(diff.keys()):
        entry = diff[key]
        status = entry["status"]
        match status:
            case "added":
                value = format_stylish(entry["value"], depth + 1)
                report += [f"{indent}+ {key}: {value}"]
            case "removed":
                value = format_stylish(entry["value"], depth + 1)
                report += [f"{indent}- {key}: {value}"]
            case "changed":
                if isinstance(entry["value"], dict):
                    value = format_stylish(entry["value"], depth + 1)
                    report += [f"{indent}  {key}: {value}"]
                else:
                    old_value, new_value = entry["value"]
                    old_value = format_stylish(old_value, depth + 1)
                    new_value = format_stylish(new_value, depth + 1)
                    report += [f"{indent}- {key}: {old_value}"]
                    report += [f"{indent}+ {key}: {new_value}"]
            case "unchanged":
                value = format_stylish(entry["value"], depth + 1)
                report += [f"{indent}  {key}: {value}"]
    report.append(f"{INDENT * (2 * depth)}" + '}')

    return SEPARATOR.join(report)