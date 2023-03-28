#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
def main() -> None:
    user_input: str = input("Input a name \n")
    for char in user_input:
        if not char.isascii():
            logging.error("Invalid input")
            sys.exit(1)

    print(f'Hello {user_input}')

if __name__ == '__main__':
    main()