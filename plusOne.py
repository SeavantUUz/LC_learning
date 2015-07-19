# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/19'


def plusOne(digits):
    c = 1
    size = len(digits)
    index = size - 1
    while index >= 0:
        m = digits[index] + c
        digits[index] = m % 10
        c = m / 10
        index -= 1
    if c:
        digits.insert(0, c)
    return digits


if __name__ == '__main__':
    print plusOne([9,9,9])

