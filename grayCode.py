# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/2'


def grayCode0(n):
    if not n:
        return [n]
    result = []
    result.append(0)
    n -= 1
    bit = 1
    while n:
        result.append(bit)
        bit = bit << 1 | 1
        n -= 1
    max_value = bit
    while bit:
        result.append(bit)
        bit = (bit << 1) & max_value
    return result


def grayCode1(n):
    return [(i>>1)^i for i in 2**n]


def grayCode(n):
    result = []
    index = 0
    result.append(0)
    while index < n:
        result += [2**index+num for num in reversed(result)]
        index += 1
    return result



if __name__ == '__main__':
    print grayCode(3)