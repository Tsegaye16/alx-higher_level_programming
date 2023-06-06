#!/usr/bin/python3
for j in range(10):
    for k in range(j+1):
        print("{}{}".format(j, k), end="")
print("".format(chr(8)), end="\n")
