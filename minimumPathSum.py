# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/18'


def minimumPathSum(grid):
    M = len(grid)
    N = len(grid[0])
    memo = dict()
    def _path(m, n, minimum):
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0:
            while n>0:
                minimum += grid[0][n]
                n -= 1
            return minimum
        elif n == 0:
            while m>0:
                minimum += grid[m][0]
                m -= 1
            return minimum
        else:
            minimum = min(_path(m-1, n, minimum), _path(m, n-1, minimum)) + grid[m][n]
            memo[(m, n)] = minimum
            return minimum
    return _path(M-1, N-1, grid[0][0])


def minimumPathSum_iter(grid):
    M = len(grid)
    N = len(grid[0])
    matrix=[[0 for y in range(N)] for x in range(M)]
    matrix[0][0] = grid[0][0]
    n = 1
    index = 0
    sum = 0
    while index < M:
        sum += grid[index][0]
        matrix[index][0] = sum
        index += 1
    index = 0
    sum = 0
    while index < N:
        sum += grid[0][index]
        matrix[0][index] = sum
        index += 1
    while n < N:
        m = 1
        while m < M:
            matrix[m][n] = min(matrix[m-1][n], matrix[m][n-1]) + grid[m][n]
            m += 1
        n += 1
    return matrix[-1][-1]

if __name__ == '__main__':
    # print minimumPathSum_iter([[1, 2], [1, 1]])
    print minimumPathSum_iter([[1]])