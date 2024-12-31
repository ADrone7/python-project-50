INDENT = "  "
SEPARATOR = '\n'
STATUS_TO_SYMBOLS = {
    "added": '+',
    "removed": '-',
    "changed": "-+",
    "unchanged": ' ',
}


def stylish(diff, depth=0):
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