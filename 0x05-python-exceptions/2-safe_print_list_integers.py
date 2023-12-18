#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = int(my_list[i])
    print("{:d}".format(value), end="")
        count += 1
    print ()
        return count
    except (ValueError, TypeError, IndexError)
        return count
