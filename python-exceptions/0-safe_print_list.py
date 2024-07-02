#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # To know the number of element print

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    # To let the code run if x greater than the length of the list
    except IndexError:
        pass

    print()
    return (count)
