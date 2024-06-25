#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argument = len(sys.argv)

    if argument <= 1:
        print("{:d} arguments.".format(argument - 1))
    elif argument == 2:
        print("{:d} argument:".format(argument - 1))
        print("{:d}: {}".format(argument - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argument - 1))
        for i in range(1, argument):
            print("{:d}: {}".format(i, sys.argv[i]))
