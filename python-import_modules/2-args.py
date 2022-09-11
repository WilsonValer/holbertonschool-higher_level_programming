#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    num = len(sys.argv)

    if num == 1:
        print("0 arguments.")
    elif num == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))
