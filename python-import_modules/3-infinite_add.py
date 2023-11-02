#!/usr/bin/python3


from sys import argv

if __name__ == '__main__':
    def my_func(argv):
        argv[1:] = [int(x) for x in argv[1:]]
        print(sum(argv[1:]))            

my_func(argv)
