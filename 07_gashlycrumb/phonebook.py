#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-16
Purpose: Phonebook
"""

import argparse
import json


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Phonebook',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name',
                        metavar='name',
                        nargs='+',
                        type=str,
                        help='Names(s)')


    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='phonebook.json')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name_list: str = args.name
    file_name: str = args.file

    lookup = json.load(file_name)

    for name in name_list:
        if name in lookup:
            print(lookup[name])
        else:
            print(f'I do not know "{name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
