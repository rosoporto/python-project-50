#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def create_parser():
    parser = argparse.ArgumentParser(
        'gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
