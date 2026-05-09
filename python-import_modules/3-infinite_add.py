#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    resultado = 0
    for i in range(1, len(argv)):
        resultado += int(argv[i])
    print(resultado)
