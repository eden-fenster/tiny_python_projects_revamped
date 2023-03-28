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

    # parser.add_argument('text',
    #                     metavar='text',
    #                     type=str,
    #                     help='Input String or File')
    #
    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='Output directory',
                        type=str,
                        default='')

    parser.add_argument('text',
                        metavar='Input',
                        nargs='+',
                        help='text or a list of input files')

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    for text in args.text:
        if not os.path.isfile(text):
            print(text.upper()+'\n')
            continue
        lines = open(text).readlines()

        output_fh = sys.stdout if not args.outdir else open(os.path.join(args.outdir, text), "wt")
        for line in lines:
            output_fh.write(line.upper())
        if args.outdir:
            output_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
