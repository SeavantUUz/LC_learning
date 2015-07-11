# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/11'


def myPow(x, n):
    if n == 0:
        return 1
    if x == 0:
        return 0
    result = 1
    if n > 0:
        remain = n
        while remain > 1:
            p = 1
            m = x
            while remain - p >= p:
                m *= m
                result *= m
                p *= 2
                remain -= p
        if remain:
            result *= x
    else:
        remain = -n
        while remain > 1:
            p = 1
            m = 1/x
            while remain - p >= p:
                m *= m
                result *= m
                p *= 2
                remain -= p
        if remain:
            result *= 1/x
    return result


if __name__ == '__main__':
    print myPow(2.0, -3)
