import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture
def get_output_files():
    with open('tests/fixtures/out_files.txt', 'r') as out_files:
        return out_files.read()


def test_generate_diff(get_output_files):
    json_file1 = 'tests/fixtures/file1.json'
    json_file2 = 'tests/fixtures/file2.json'

    result = generate_diff(json_file1, json_file2, to_output=False)

    assert result.strip() == get_output_files.strip()