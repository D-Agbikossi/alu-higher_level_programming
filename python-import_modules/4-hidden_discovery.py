#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for i in range(len(names)):
        if names[i][:2] != '__':
            print(names[i])
