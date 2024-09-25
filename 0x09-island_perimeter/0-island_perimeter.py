#!/usr/bin/python3
""" island perimeter problem """


def island_perimeter(grid):
    """ calculate island perimeter """
    if grid is None or not isinstance(grid, list):
        return 0
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    perimeter = 0
    height = len(grid)
    length = len(grid[0])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                if j < length - 1:
                    if grid[i][j + 1] == 0:
                        perimeter += 1
                else:
                    perimeter += 1
                if j > 0:
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                else:
                    perimeter += 1

                if i < height - 1:
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                else:
                    perimeter += 1
                if j > 0:
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                else:
                    perimeter += 1
    return perimeter
