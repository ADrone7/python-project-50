from pathlib import Path

FILE1 = "file1"
FILE2 = "file2"
RESULT = "file1_file2_diff.txt"
FILE1_RECURSIVE = "file1_recursive"
FILE2_RECURSIVE = "file2_recursive"
RESULT_RECURSIVE = "file1_file2_diff_recursive.txt"
FORMATS = 'json', 'yaml'


def get_test_data_path() -> Path:
    return Path(__file__).parent / "test_data"


def read_file(file_name: str) -> str:
    path = get_test_data_path() / file_name
    return path.read_text()