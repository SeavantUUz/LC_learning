# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/12'


def reverseBits(n):
    value = 0
    count = 31
    while count:
        r = n&1
        n >>= 1
        value |= r
        value <<= 1
        count -= 1
    return value | n


if __name__ == '__main__':
    print bin(reverseBits(2147483648))

