# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/7'


def convertToTitle(n):
    result = []
    while n != 0:
        r = (n-1) % 26 + 1
        result.insert(0, chr(r+64))
        n = (n-1) / 26
    return ''.join(result)


if __name__ == '__main__':
    print convertToTitle(58)