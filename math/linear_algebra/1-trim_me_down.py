#!/usr/bin/env python3

matrix = [
    [1, 3, 9, 4, 5, 8],
    [2, 4, 7, 3, 4, 0],
    [0, 3, 4, 6, 1, 5]
]

the_middle = []
n_colmn = len(matrix[0])   

if n_colmn % 2 == 0:

    mid1 = n_colmn//2 - 1
    mid2 = n_colmn//2
    for row in matrix:
        the_middle.append([row[mid1], row[mid2]])
else:
    mid = n_colmn//2
    for row in matrix:
        the_middle.append([row[mid]])

print("The middle columns of the matrix are: {}".format(the_middle))
