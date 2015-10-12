# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/12'


def countDigitOne(n):
    if n< 1:
        return 0
    if n < 10:
        return 1
    m = 1
    count = 0
    while m<=n:
        count += (n/m + 8) /10 * m + (n/m % 10 == 1) * (n%m + 1)
        m *= 10
    return count

