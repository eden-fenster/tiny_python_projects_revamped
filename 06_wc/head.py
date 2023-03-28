#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-11
Purpose: Emulate head
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')
    parser.add_argument('-n',
                        '--lines',
                        help='Count lines',
                        type=int,
                        default=10)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    line_number = 0
    for file_handle in args.file:
        if len(args.file) > 1:
            print(file_handle.name)
        for _ in range(0, args.lines):
            line = file_handle.readline()
            print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
