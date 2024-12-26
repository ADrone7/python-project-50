from pathlib import Path


def read_file(file_name: str) -> str:
    path = Path(__file__).parent / "test_data" / file_name
    return path.read_text()