# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com
"""
# 1. Napisz funkcję która na wejściu dostaje macierz NxN i wyświetla ją w "spiralny sposób": https://graphicheck.com/image/cache/catalog/ad/spiral-assets-affinity-designer-500x500.png


def get_matrix_as_spiral(matrix):
    """This function takes a NxN matrix and prints it as a spiral."""

    num_of_rows = len(matrix)
    top = 0
    bottom = num_of_rows - 1
    left = 0
    right = num_of_rows - 1

    result = []
    while top <= bottom and left <= right:
        # Upper left corner, append all numbers till the right one
        result.extend(matrix[top][i] for i in range(left, right + 1))
        top += 1

        # Upper right corner, adding all numbers till the bottom
        result.extend(matrix[i][right] for i in range(top, bottom + 1))
        right -= 1

        # Lower left corner, moving towards right, adding all numbers on the way
        result.extend(matrix[bottom][i] for i in range(right, left - 1, -1))
        bottom -= 1

        # Lower right corner, moving upwards
        result.extend(matrix[i][left] for i in range(bottom, top - 1, -1))
        left += 1
    return result


if __name__ == "__main__":
    assert get_matrix_as_spiral([]) == []
    assert get_matrix_as_spiral([1]) == [1]
    assert get_matrix_as_spiral([[1, 2], [3, 4]]) == [1, 2, 4, 3]

    assert get_matrix_as_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]

    matrix5x5 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    assert get_matrix_as_spiral(matrix5x5) == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        25,
        24,
        23,
        22,
        21,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        19,
        18,
        17,
        12,
        13,
    ]
