SEPARATOR = '\n'


def convert(value) -> str:
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f"'{value}'"
    elif isinstance(value, (dict, list, tuple, set)):
        value = '[complex value]'
    else:
        value = str(value)
    return value


def format_plain(diff: dict) -> str:
    report = []

    def walk_dict(subdiff: dict, parent: str = '') -> None:
        for key, data in subdiff.items():
            status = data['status']
            if status == "added":
                report.append((f"Property '{parent}{key}' was added with "
                               f"value: {convert(data['value'])}"))
                continue
            if status == "removed":
                report.append(f"Property '{parent}{key}' was removed")
                continue
            if status == "nested change":
                walk_dict(data['value'], f"{parent}{key}.")
                continue
            if status == "changed":
                old = data['old_value']
                new = data['new_value']
                report.append((f"Property '{parent}{key}' was updated. From " 
                f"{convert(old)} to {convert(new)}"))
    walk_dict(diff)

    return SEPARATOR.join(sorted(report))