# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/16'


def rangeBitwiseAnd(m, n):
    factor = 0
    while m != n:
        m >>= 1
        n >>= 1
        factor += 1
    n <<= factor
    return n


if __name__ == '__main__':
    print rangeBitwiseAnd(5, 7)