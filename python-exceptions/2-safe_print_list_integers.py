#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, cont = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            cont += 1
        i += 1
    print()
    return cont
