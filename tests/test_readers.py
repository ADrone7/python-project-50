from gendiff.readers import read_json, read_yaml
from tests.utility import FILE1, get_test_data_path

PATH = get_test_data_path()
EXPECTED = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


def test_read_json():
    actual = read_json(str(PATH / f'{FILE1}.json'))
    assert actual["host"] == EXPECTED["host"]
    assert actual["timeout"] == EXPECTED["timeout"]
    assert actual["proxy"] == EXPECTED["proxy"]
    assert actual["follow"] == EXPECTED["follow"]


def test_read_yaml():
    actual = read_yaml(str(PATH / f'{FILE1}.yaml'))
    assert actual["host"] == EXPECTED["host"]
    assert actual["timeout"] == EXPECTED["timeout"]
    assert actual["proxy"] == EXPECTED["proxy"]
    assert actual["follow"] == EXPECTED["follow"]