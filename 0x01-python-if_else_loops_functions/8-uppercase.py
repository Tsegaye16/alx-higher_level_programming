#!/usr/bin/python3
def uppercase(str):
    list1 = list(str)
    for i in range(len(list1)):
        if ord(list1[i]) > 96 and ord(list1[i]) < 123:
            list1[i] = chr(ord(list1[i]) - 32)
    print("{}".format("".join(list1)))
