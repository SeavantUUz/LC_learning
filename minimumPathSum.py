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

if __name__ == '__main__':
    print minimumPathSum([[1, 2], [1, 1]])