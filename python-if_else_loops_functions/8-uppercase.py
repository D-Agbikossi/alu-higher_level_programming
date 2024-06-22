#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n >= 97 and n <= 122:
            m = n-32
        else:
            m = n

        print("{:c}".format(m), end="")
    print()
