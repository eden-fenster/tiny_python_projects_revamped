#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-16
Purpose: Rock the Casbah
"""

import argparse



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find # of occurrences of a letter in a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='What we want to find')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=str,
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_name: str = args.file
    text: str = args.text

    file_handle = open(file_name, "rt")
    data = file_handle.read()
    occurrences = data.count(text)
    print(f'{text} appears {occurrences} times')


# --------------------------------------------------
if __name__ == '__main__':
    main()
