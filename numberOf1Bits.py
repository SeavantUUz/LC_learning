# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/13'


def hammingWeight(n):
    count = 0
    while n:
        n = n&(n-1)
        count += 1
    return count


if __name__ == '__main__':
    print hammingWeight(3)