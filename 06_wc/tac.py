#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-11
Purpose: Emulate cat
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
                        '--count',
                        help='Count lines',
                        action="store_true",
                        default=False)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    line_number = args.count
    for file_handle in args.file:
        for line in reversed(file_handle.readlines()):
            line_number -= 1
            prefix = ""
            if 0:
                prefix = f'{line_number:8} '
            print(prefix+line, end='')

# --------------------------------------------------
if __name__ == '__main__':
    main()
