#!/usr/bin/env python3
import argparse


def create_parser():
    parser = argparse.ArgumentParser('gendiff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    return parser


def main():
    parser = create_parser()
    parser.parse_args()


if __name__ == '__main__':
    main()
