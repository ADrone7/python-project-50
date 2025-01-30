SEPARATOR = '\n'


def convert(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f"'{value}'"
    elif hasattr(value, '__iter__'):
        value = '[complex value]'
    return value


def plain(diff, path=None):
    report = []

    def walk(diff, parent=''):
        for key, data in diff.items():
            status = data['status']
            value = data['values']
            if status == "added":
                report.append((f"Property '{parent}{key}' was added with "
                               f"value: {convert(value)}"))
                continue
            if status == "removed":
                report.append(f"Property '{parent}{key}' was removed")
                continue
            if status == "changed":
                if isinstance(value, dict):
                    walk(value, f"{parent}{key}.")
                    continue
                report.append((f"Property '{parent}{key}' was updated. From " 
                              f"{convert(value[0])} to {convert(value[1])}"))
    walk(diff)

    return SEPARATOR.join(sorted(report))