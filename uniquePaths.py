# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/17'

def uniquePaths(m, n):
    memo = dict()
    def _unique(m, n):
        if memo.get((m, n)):
            return memo[(m, n)]
        if m == 1 or n == 1:
            return 1
        else:
            result = _unique(m-1, n)  + _unique(m, n-1)
            memo[(m, n)] = result
            return result
    return _unique(m, n)

if __name__ == '__main__':
    print uniquePaths(3, 2)
