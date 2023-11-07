#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
    for row in matrix:
        row_index = matrix.index(row)
        for element in matrix[row_index]:
            print('{:d}'.format(element), end='')
            if matrix[row_index].index(element) != (len(matrix[row_index])-1):
                print(' '.format(), end='')
            else:
                print()
