#!/usr/bin/python3
upper = False

for letter in range(122, 96, -1):
    char = chr(letter)
    if upper:
        char = char.upper()
    else:
        char = char.lower()

    print("{}".format(char), end="")

    upper = not upper
