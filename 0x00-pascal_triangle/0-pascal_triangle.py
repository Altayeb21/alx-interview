#!/usr/bin/python3
""" create pascal triangle """


def pascal_triangle(n):
    """ return a list of lists of integers representing the pascal's
    triangle of n"""
    if n <= 0:
        return []
    ps_tri = []
    for i in range(n):
        row = []
        for j in range(i+1):
            new = 1
            if i != 0 and j > 0 and j < i:
                new = ps_tri[i - 1][j] + ps_tri[i - 1][j - 1]
            row.append(new)
        ps_tri.append(row)

    return ps_tri
