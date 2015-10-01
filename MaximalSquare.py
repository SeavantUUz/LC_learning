# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/1'


def maximalSquare(matrix):
    if not matrix:
        return 0
    column = len(matrix)
    row = len(matrix[0])
    for i in xrange(column):
        matrix[i] = [int(num) for num in matrix[i]]
        for j in xrange(row):
            if matrix[i][j] and i and j:
                matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
    return max([max(line) ** 2 for line in matrix])


if __name__ == '__main__':
    print maximalSquare(['000', '000', '000', '000'])

