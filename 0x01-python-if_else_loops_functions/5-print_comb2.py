#!/usr/bin/python3
for k in range(100):
    print("{:0>2}".format(k), end=", " if k < 99 else "\n")
