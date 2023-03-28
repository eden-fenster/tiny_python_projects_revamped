#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-11
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')
    parser.add_argument('-c',
                        '--characters',
                        help='Number of characters',
                        action="store_true",
                        default=False)
    parser.add_argument('-l',
                        '--lines',
                        help='Number of lines',
                        action="store_true",
                        default=False)
    parser.add_argument('-w',
                        '--words',
                        help='Number of words',
                        action="store_true",
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    total_lines, total_bytes, total_words = 0, 0, 0
    for file_handle in args.file:
        num_lines_in_file, num_bytes_in_file, num_words_in_files = 0, 0, 0
        for line in file_handle:
            num_lines_in_file += 1
            num_bytes_in_file += len(line)
            num_words_in_files += len(line.split())

        total_lines += num_lines_in_file
        total_bytes += num_bytes_in_file
        total_words += num_words_in_files

        if args.lines:
            print(f'{num_lines_in_file:8}', end=" ")
        if args.words:
            print(f'{num_words_in_files:8}', end=" ")
        if args.characters:
            print(f'{num_bytes_in_file:8}', end=" ")
        print(file_handle.name)

    if len(args.file) > 1:
        if args.lines:
            print(f'{total_lines:8}', end=" ")
        if args.words:
            print(f'{total_words:8}', end=" ")
        if args.characters:
            print(f'{total_bytes:8}', end=" ")
        print('total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
