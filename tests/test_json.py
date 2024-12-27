from gendiff.read_json import read_json
from tests.utility import get_test_data_path

FILE1 = "file1.json"
FILE2 = "file2.json"


def test_read_json():
    path = get_test_data_path() / FILE1
    expected = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    actual = read_json(path)
    assert actual["host"] == expected["host"]
    assert actual["timeout"] == expected["timeout"]
    assert actual["proxy"] == expected["proxy"]
    assert actual["follow"] == expected["follow"]