#!/usr/bin/env python3
""""
# Purpose: Say hello
# If it gets a name, call main
"""

import argparse


def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(description='say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """"The main class"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
