#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
def main() -> None:
    user_input: str = input("Input 'Hello World' \n")
    if user_input != 'Hello World':
        logging.error("Invalid input")
        sys.exit(1)
    print(user_input)

if __name__ == '__main__':
    main()