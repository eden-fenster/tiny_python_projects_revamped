#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-01
Purpose: Crow's Nest
Edit Date: 2023-03-27
"""


# --------------------------------------------------
import random
import logging
import sys
from typing import List

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
VOWELS: str = 'aeiou'





# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    word: str = input("Input a word \n")
    side: str = input("Input a side \n")
    if side is not 'larboard' and side is not 'starboard':
        logging.error("Invalid input")
        sys.exit(1)

    print(user_greeting(word=word, side=side))


def user_greeting(word: str, side: str) -> str:
    random_greetings: List[str] = ['Ahoy', 'Hello', 'Hola', 'Salut', 'Ciao']
    greeting: str = random.choice(random_greetings)
    if word is '':
        word = "Unknown"
    if word[0].isupper():
        article = 'An' if word[0].lower() in VOWELS else 'A'
    else:
        article = 'an' if word[0].lower() in VOWELS else 'a'
    return f'{greeting}, Captain, {article} {word} off the {side} bow!'


def test_user_greeting():
    assert user_greeting(word='larboard', side='larboard') == 'Salut, Captain, a larboard off the larboard bow!'


# --------------------------------------------------
if __name__ == '__main__':
    main()
