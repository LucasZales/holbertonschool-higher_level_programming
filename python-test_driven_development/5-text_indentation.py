#!/usr/bin/python3
"""Module for Indentation after Certain Chars"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text , str):
        raise TypeError("text must be a string")

    idx = 0
    length = len(text)

    while idx < length:
        print(text[idx], end="")

        if text[idx] in ".?:":
            print("\n")

            idx += 1
            while idx < length and text[idx] == " ":
                idx += 1
            continue

        idx += 1
