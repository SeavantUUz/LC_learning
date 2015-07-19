# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/19'


def addBinary(a, b):
    a = map(int, a)
    b = map(int, b)
    result = []
    a_length = len(a)
    b_length = len(b)
    index_a = a_length - 1
    index_b = b_length - 1
    c = 0
    while index_a >= 0 and index_b >= 0:
        value = a[index_a] + b[index_b] + c
        result.insert(0, value % 2)
        c = value / 2
        index_a -= 1
        index_b -= 1

    if index_a >= 0 :
        index = index_a
        remain = a
    elif index_b >= 0:
        index = index_b
        remain = b
    else:
        index = -1
    while index >=0:
        value = remain[index] + c
        result.insert(0, value % 2)
        c = value / 2
        index -= 1
    if c:
        result.insert(0, c)
    return ''.join(map(str, result))


if __name__ == '__main__':
    print addBinary('11', '1')
