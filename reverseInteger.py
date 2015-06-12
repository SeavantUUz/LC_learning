# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/12'


def reverseInteger(x):
    if x > 2**31-1 or x < -2**31:
        return 0
    if x < 0:
        sign = -1
        x = abs(x)
    else:
        sign = 1
    result = 0
    while x:
        m = x%10
        result = result * 10 + m
        x /= 10
    r = sign * result
    if r > 2**31-1 or r < - 2** 31:
        return 0
    else:
        return r


if __name__ == '__main__':
    print reverseInteger(1000000003)

