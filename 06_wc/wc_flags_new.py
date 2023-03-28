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
    if True not in [args.characters, args.words, args.lines]:
        args.characters = args.words = args.lines = True

    total_lines, total_bytes, total_words = 0, 0, 0
    for file_handle in args.file:
        num_lines_in_file, num_bytes_in_file, num_words_in_file = 0, 0, 0
        for line in file_handle:
            num_lines_in_file += 1
            num_bytes_in_file += len(line)
            num_words_in_file += len(line.split())

        total_lines += num_lines_in_file
        total_bytes += num_bytes_in_file
        total_words += num_words_in_file

        output_line = format_output_line(
            args=args, name=file_handle.name, line_count=num_lines_in_file,
            word_count=num_words_in_file, byte_count=num_bytes_in_file)
        print(output_line)

    if len(args.file) > 1:
        output_line = format_output_line(
            args=args, name="total", line_count=total_lines,
            word_count=total_words, byte_count=total_bytes)
        print(output_line)


# pylint: disable=missing-function-docstring
def format_output_line(args, name, line_count, word_count, byte_count):
    raw_output = []
    if args.lines:
        raw_output.append(f'{line_count:8}')
    if args.words:
        raw_output.append(f'{word_count:8}')
    if args.characters:
        raw_output.append(f'{byte_count:8}')
    raw_output.append(name)
    return " ".join(raw_output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
