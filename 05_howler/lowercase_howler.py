#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-08
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input String or File')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')
    parser.add_argument('-e',
                        '--ee',
                        help='Make text lowercase',
                        action="store_true",
                        default=False)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    if args.ee:
        processed_text = args.text.lower()
    else:
        processed_text = args.text.upper()
    out_fh.write(processed_text + '\n')
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()