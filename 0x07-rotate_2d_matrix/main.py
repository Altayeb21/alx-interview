#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 13, 3, 10, 17, 26],
              [4, 5, 14, 11, 18, 27],
              [7, 8, 9, 12, 19, 28],
              [2, 6, 15, 16, 20, 29],
              [21, 22, 23, 24, 25, 30],
              [31, 32, 33, 34, 35, 36]]
    for m in matrix:
        print(m)
    print("----------------")
    rotate_2d_matrix(matrix)
    for m in matrix:
        print(m)
