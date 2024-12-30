from gendiff import generate_diff
from tests.utility import (
    FILE1,
    FILE2,
    FORMATS,
    RESULT,
    get_test_data_path,
    read_file,
)


def test_generate_diff():
    expected = read_file(RESULT)
    test_data_path = get_test_data_path()

    for format in FORMATS:
        file_path1 = str(test_data_path / f"{FILE1}.{format}")
        file_path2 = str(test_data_path / f"{FILE2}.{format}")
        actual = generate_diff(file_path1, file_path2)
        assert actual == expected
