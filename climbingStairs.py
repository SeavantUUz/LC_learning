# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/20'


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = [1, 1, 2]
    index = 3
    while index <= n:
        value = result[index-1] + result[index-2]
        result.append(value)
        index += 1
    return result[n]


if __name__ == '__main__':
    print climbStairs(4)