# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/8'


def titleToNumber(s):
    result = 0
    for c in s:
        result = result * 26 + ord(c) - 64
    return result


if __name__ == '__main__':
    print titleToNumber('HRL')