#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-01
Purpose: Crow's Nest
Edit Date: 2023-03-27
"""
import logging
import sys

# --------------------------------------------------
VOWELS = 'aeiou'
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    word = input ("Input a word \n")
    side = input ("Input a side \n")

    if side is not 'larboard' and side is not 'starboard':
        logging.error("Invalid input")
        sys.exit(1)

    if word is '':
        word = "Unknown"
    if word[0].isupper():
        article = 'An' if word[0].lower() in VOWELS else 'A'
    else:
        article = 'an' if word[0].lower() in VOWELS else 'a'

    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
