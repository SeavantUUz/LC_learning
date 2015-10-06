# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/6'


def isPowerOfTwo(n):
    if n==0:
        return False
    return n & (n-1) == 0