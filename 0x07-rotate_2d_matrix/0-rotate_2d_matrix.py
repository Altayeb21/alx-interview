#!/usr/bin/python3
""" rotate 2D matrix module """


def rotate_2d_matrix(matrix):
    """ rotate 2d matrix 90 degrees clockwise """
    n = len(matrix)
    if n <= 1:
        return
    tmp = 0
    start = 0
    last = n - 1
    limit = n - 1
    for j in range(int(n/2)):
        for i in range(limit):
            tmp = matrix[start + i][last]
            matrix[start + i][last] = matrix[start][start + i]
            matrix[start][start + i] = matrix[last - i][start]
            matrix[last - i][start] = matrix[last][last - i]
            matrix[last][last - i] = tmp
        limit -= 2
        start += 1
        last -= 1
