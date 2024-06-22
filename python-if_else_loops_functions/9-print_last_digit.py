#!/usr/bin/python3
def print_last_digit(number):
    l = int(str(number)[-1])
    print("{:d}".format(l), end="")
    return(l)
