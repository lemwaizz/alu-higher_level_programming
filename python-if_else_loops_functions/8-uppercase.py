#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            char = chr(ord(ch) - 32)
        print("{}".format(char), end='')
    print('')
    
