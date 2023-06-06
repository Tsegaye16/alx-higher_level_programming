#!/usr/bin/python3
for m in range(10):
    for n in range(m + 1, 10):
        print(
            "{}{}".format(m, n),
            end=", " if int(str(m) + str(n)) < 89 else "\n"
            )
