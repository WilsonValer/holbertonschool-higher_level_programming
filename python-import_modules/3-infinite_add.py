#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num_argu = len(sys.argv)
    suma = 0
    for i in range(1, num_argu):
        suma += int(sys.argv[i])
    print(suma)
