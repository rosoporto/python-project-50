#!/usr/bin/env python3
import os
import json
import yaml


def load_data(_file):
    _, ext = os.path.splitext(_file)
    with open(_file, 'r') as f:
        if ext == '.json':
            data = json.load(f)
        elif ext in ['.yml', '.yaml']:
            data = yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file format: {ext}')
        return data


def main():
    yaml_file = 'tests/fixtures/file1.yml'
    result = load_data(yaml_file)
    print(result)


if __name__ == '__main__':
    main()
