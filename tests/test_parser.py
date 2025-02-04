import pytest

from gendiff.parser import parse
from tests.utility import FILE1, read_file

EXPECTED = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


@pytest.mark.parametrize('input_format', [('json'), ('yaml')])
def test_parse(input_format):
    file_path = f'{FILE1}.{input_format}'
    content = read_file(file_path)
    actual = parse(content, input_format)
    assert actual == EXPECTED