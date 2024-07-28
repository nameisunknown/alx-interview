#!/usr/bin/python3

"""This module is about pascal_triangle() and for alx-interview"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers

    Args:
        n (Integer): Represents the range of rows for the triangle
    """

    list_toBeReturned = []
    if n <= 0:
        return []

    list_toBeReturned = [[] for i in range(n)]

    for row in range(n):
        for column in range(row + 1):
            if column == 0 or column == row:
                list_toBeReturned[row].append(1)
            else:
                list_toBeReturned[row].append(
                    list_toBeReturned[row - 1][column - 1] + list_toBeReturned[row - 1][column]
                    )

    return list_toBeReturned

