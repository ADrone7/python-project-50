from pathlib import Path


def get_test_data_path():
    return Path(__file__).parent / "test_data"


def read_file(file_name: str) -> str:
    path = get_test_data_path() / file_name
    return path.read_text()