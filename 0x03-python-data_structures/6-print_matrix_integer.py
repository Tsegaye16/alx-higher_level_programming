#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            print(
                "{:d}".format(line[col]),
                end="" if col == len(row) - 1 else " ")
        print("")
