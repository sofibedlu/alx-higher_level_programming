#!/usr/bin/python3
n = 1
for i in range(122, 96, -1):
    if n % 2 == 0:
        i = i - 32
    print("{}".format(char(i)), end="")
    n += 1
