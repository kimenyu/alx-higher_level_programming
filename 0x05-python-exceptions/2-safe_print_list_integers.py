#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=' ')
                count += 1
        except IndexError:
            # x is bigger than the length of my_list
            raise
    print()
    return count
