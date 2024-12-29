from gendiff.diff import generate_diff
from tests.utility import get_test_data_path, read_file

FILE1 = "file1.json"
FILE2 = "file2.json"


def test_generate_diff():
    test_data_path = get_test_data_path()
    file_path1 = test_data_path / FILE1
    file_path2 = test_data_path / FILE2
    expected = read_file("json_diff.txt")
    actual = generate_diff(file_path1, file_path2)
    assert actual == expected
