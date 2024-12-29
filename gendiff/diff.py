from gendiff.read_json import read_json

INDENT = "  "
SEPARATOR = '\n'
STATUS_TO_SYMBOLS = {
    "added": '+',
    "removed": '-',
    "changed": "-+",
    "unchanged": ' ',
}


def generate_diff(file_path1: str, file_path2: str) -> str:
    content1 = read_json(file_path1)
    content2 = read_json(file_path2)

    difference = {}
    keys = content1.keys() | content2.keys()
    for key in keys:
        result = {}
        if key not in content1:
            result["status"] = "added"
            result["values"] = content2[key],
        elif key not in content2:
            result["status"] = "removed"
            result["values"] = content1[key],
        elif content1[key] == content2[key]:
            result["status"] = "unchanged"
            result["values"] = content1[key],
        else:
            result["status"] = "changed"
            result["values"] = content1[key], content2[key]
        difference[key] = result
    
    report = ['{']
    for key in sorted(keys):
        entry = difference[key]
        status = entry["status"]
        values = entry["values"]
        symbols = STATUS_TO_SYMBOLS[status]
        for symbol, value in zip(symbols, values):
            if isinstance(value, bool):
                value = str(value).lower()
            string = f"{INDENT}{symbol} {key}: {value}"
            report.append(string)
    report.append('}')

    return SEPARATOR.join(report)