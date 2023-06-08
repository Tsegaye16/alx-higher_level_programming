#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_of_args = len(argv)
    total = 0
    for k in range(1, num_of_args):
        total += int(argv[k])
    print("{:d}".format(total))
