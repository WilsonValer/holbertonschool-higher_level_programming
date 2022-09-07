#!/usr/bin/python3
for j in range(97, 123):
    if (j == 113) or (j == 101):
        continue
    else:
        print("{}".format(chr(j)), end='')
