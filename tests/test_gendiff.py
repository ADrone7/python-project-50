import subprocess

from tests.utility import read_file


def test_gendiff():
    expected = read_file("gendiff_result.txt")
    actual = subprocess.run(["uv", "run", "gendiff", "-h"],
                            capture_output=True, text=True)
    assert expected == actual.stdout
