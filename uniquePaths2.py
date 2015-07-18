# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/18'

def uniquePath2(obstacleGrid):
    M = len(obstacleGrid)
    N = len(obstacleGrid[0])
    memo = dict()
    def _unique(m, n):
        if (m, n) in memo:
            return memo[(m, n)]
        elif m < 0 or n < 0 or obstacleGrid[m][n]:
            return 0
        elif m==0 and n==0:
            return 1
        else:
            result = _unique(m-1, n) + _unique(m, n-1)
            memo[(m, n)] = result
            return result
    return _unique(M-1, N-1)

if __name__ == '__main__':
    print uniquePath2([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print uniquePath2([[0]])
    print uniquePath2([[1, 0]])
