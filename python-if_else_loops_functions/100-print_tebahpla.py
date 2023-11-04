#!/usr/bin/python3
for ch in range(122, 97, -2):
    alpha = chr(ch)
    for char in alpha:
        print("{}{}".format(char, chr(ord(char) - 33)), end='')
