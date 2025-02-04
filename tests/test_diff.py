import pytest

from gendiff import generate_diff
from tests.utility import (
    FILE1,
    FILE1_RECURSIVE,
    FILE2,
    FILE2_RECURSIVE,
    FORMATS,
    RESULT_RECURSIVE_JSON,
    RESULT_RECURSIVE_PLAIN,
    RESULT_RECURSIVE_STYLISH,
    RESULT_STYLISH,
    get_test_data_path,
    read_file,
)


@pytest.mark.parametrize("file1,file2,result,output_format", [
    (FILE1, FILE2, RESULT_STYLISH, 'stylish'),
    (FILE1_RECURSIVE, FILE2_RECURSIVE, RESULT_RECURSIVE_STYLISH, 'stylish'),
    (FILE1_RECURSIVE, FILE2_RECURSIVE, RESULT_RECURSIVE_PLAIN, 'plain'),
    (FILE1_RECURSIVE, FILE2_RECURSIVE, RESULT_RECURSIVE_JSON, 'json'),
    ])
def test_generate_diff(file1, file2, result, output_format):
    expected = read_file(result)
    test_data_path = get_test_data_path()

    for input_format in FORMATS:
        file_path1 = str(test_data_path / f"{file1}.{input_format}")
        file_path2 = str(test_data_path / f"{file2}.{input_format}")
        actual = generate_diff(file_path1, file_path2, output_format)
        assert actual == expected