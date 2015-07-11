# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/9'


def rotate0(matrix):
    n = len(matrix)
    new_matrix = []
    index = 0
    while index < n:
        j = n - 1
        new_line = []
        while j >= 0:
           new_line.append(matrix[j][index])
           j -= 1
        new_matrix.append(new_line)
        index += 1
    return new_matrix


def rotate(matrix):
    n = len(matrix)
    i = 1
    while i < n:
        j = 0
        while j < i:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1
        i += 1
    index = 0
    while index < n:
        i = 0
        j = n - 1
        while i < j:
            matrix[index][i], matrix[index][j] = matrix[index][j], matrix[index][i]
            i += 1
            j -= 1
        index += 1
    print matrix


if __name__ == '__main__':
    rotate([[1,2,3], [4,5,6], [7,8,9]])

