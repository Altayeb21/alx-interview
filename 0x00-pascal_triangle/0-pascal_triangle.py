#!/usr/bin/python3
""" create pascal tringle of n """


def pascal_triangle(n):
    """ return a list of lists of integers representing the pascal's
    triangle of n """
    if n <= 0:
        return []
    tri = []
    for i in range(n):
        tri.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                tri[i].append(1)
            else:
                tri[i].append(tri[i - 1][j] + tri[i - 1][j - 1])
    return tri
