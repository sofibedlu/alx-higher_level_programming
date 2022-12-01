#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    if len(argv) < 3:
        print(result)
    elif len(argv) >= 3:
        for i in argv:
            if i == argv[0]:
                continue
            result += int(i)
        print(result)
