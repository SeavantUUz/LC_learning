# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/9'


def trailingZeroes(n):
    count = 0
    de = 5
    while de <= n:
        count += n / de
        de *= 5
    return count


def factor(n):
    result = 1
    for i in xrange(1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    print factor(25)
    print trailingZeroes(30)