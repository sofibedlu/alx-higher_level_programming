#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    if len(argv) < 2:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(1, argv[1]))
    elif len(argv) > 2:
        n = 1
        print("{} arguments:".format(len(argv) - 1))
        for lists in argv:
            if lists == argv[0]:
                continue
            print("{}: {}".format(n, argv[n]))
            n += 1
