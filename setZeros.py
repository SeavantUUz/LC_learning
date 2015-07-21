# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/21'


def setZeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    xs = set()
    ys = set()
    for i in xrange(n):
        for j in xrange(m):
            if matrix[i][j] == 0:
                xs.add(i)
                ys.add(j)
    for x in xs:
        for i in xrange(m):
            matrix[x][i] = 0

    for y in ys:
        for j in xrange(n):
            matrix[j][y] = 0

    print matrix


if __name__ == '__main__':
    setZeros([[1, 0], [1, 1]])

