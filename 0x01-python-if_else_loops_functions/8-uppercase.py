#!/usr/bin/python3
def uppercase(str):
    string = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            string += chr(ord(ch) - 32)
        else:
            string += ch
    print(string)
