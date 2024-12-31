from gendiff import generate_diff
from tests.utility import (
    FILE1,
    FILE1_RECURSIVE,
    FILE2,
    FILE2_RECURSIVE,
    FORMATS,
    RESULT_RECURSIVE_PLAIN,
    RESULT_RECURSIVE_STYLISH,
    RESULT_STYLSIH,
    get_test_data_path,
    read_file,
)


def test_generate_diff_stylish():
    expected = read_file(RESULT_STYLSIH)
    test_data_path = get_test_data_path()

    for format in FORMATS:
        file_path1 = str(test_data_path / f"{FILE1}.{format}")
        file_path2 = str(test_data_path / f"{FILE2}.{format}")
        actual = generate_diff(file_path1, file_path2)
        assert actual == expected


def test_generate_diff_recursive_stylish():
    expected = read_file(RESULT_RECURSIVE_STYLISH)
    test_data_path = get_test_data_path()

    for format in FORMATS:
        file_path1 = str(test_data_path / f"{FILE1_RECURSIVE}.{format}")
        file_path2 = str(test_data_path / f"{FILE2_RECURSIVE}.{format}")
        actual = generate_diff(file_path1, file_path2)
        assert actual == expected


def test_generate_diff_recursive_plain():
    expected = read_file(RESULT_RECURSIVE_PLAIN)
    test_data_path = get_test_data_path()

    for format in FORMATS:
        file_path1 = str(test_data_path / f"{FILE1_RECURSIVE}.{format}")
        file_path2 = str(test_data_path / f"{FILE2_RECURSIVE}.{format}")
        actual = generate_diff(file_path1, file_path2)
        assert actual == expected
