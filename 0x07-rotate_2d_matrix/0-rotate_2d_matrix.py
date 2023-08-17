#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotates an n x n 2D matrix 90 degrees clockwise
    """
    temp = []
    for i in range(len(matrix)):
        temp.append([])

    count = -1
    for row in matrix:
        temp_count = 0
        for i in range(len(row)):
            temp[temp_count].append(matrix[count][temp_count])
            temp_count += 1
        count -= 1
    count = 0
    for row in temp:
        temp_count = 0
        for item in row:
            matrix[count][temp_count] = item
            temp_count += 1
        count += 1


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    for row in matrix:
        print(row)
    rotate_2d_matrix(matrix)
    print("==============================")
    for row in matrix:
        print(row)
