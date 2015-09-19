# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/19'


def countPrimes(n):
    if n < 2:
        return 0
    result = [1] * n
    result[0] = result[1] = 0
    for i in xrange(2, n):
        if result[i]:
            for j in xrange(2, (n-1) / i + 1):
                result[i*j] = 0
    return sum(result)


if __name__ == '__main__':
    print countPrimes(2)

