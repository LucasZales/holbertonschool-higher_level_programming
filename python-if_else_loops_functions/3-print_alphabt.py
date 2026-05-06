#!/usr/bin/python3
for letra in range(97, 123):
    if letra != 101 and letra != 113:
        print("{}".format(chr(letra)), end="")
