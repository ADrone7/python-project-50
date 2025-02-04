import pytest

from gendiff.reader import get_format, read_file
from tests.utility import FILE1, get_test_data_path

EXPECTED = '''{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
}'''


@pytest.mark.parametrize('file_name,format', [(FILE1, 'json')])
def test_read_file(file_name, format):
    path = get_test_data_path() / f"{file_name}.{format}"
    assert read_file(path) == EXPECTED


@pytest.mark.parametrize('file_path,format', [
    ('root/something/file.json', 'json'), 
    ('asdfds.yaml', 'yaml'),
    ])
def test_get_format(file_path, format):
    assert get_format(file_path) == format