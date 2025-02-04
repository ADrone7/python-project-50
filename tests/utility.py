from pathlib import Path

FILE1 = "file1"
FILE2 = "file2"
RESULT_STYLISH = "file1_file2_stylish.txt"
RESULT_RECURSIVE_JSON = "file1_file2_recursive_json.txt"
RESULT_RECURSIVE_STYLISH = "file1_file2_recursive_stylish.txt"
RESULT_RECURSIVE_PLAIN = "file1_file2_recursive_plain.txt"
FILE1_RECURSIVE = "file1_recursive"
FILE2_RECURSIVE = "file2_recursive"
FORMATS = 'json', 'yaml'


def get_test_data_path() -> Path:
    return Path(__file__).parent / "test_data"


def read_file(file_name: str) -> str:
    path = get_test_data_path() / file_name
    return path.read_text()