#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'}

    #Method 4 : List comprehension - one line for loop inside square brackets
    print(''.join([jumper.get(char, char) for char in args.text]))


# --------------------------------------------------
if __name__ == '__main__':
    main()