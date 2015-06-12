# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/13'

def atoi(str):
    size = len(str)
    i = 0
    while i < size and str[i] == ' ':
        i += 1
    if i == size:
        return 0
    if str[i] == '-':
        sign = -1
        i += 1
    elif str[i] == '+':
        sign = 1
        i += 1
    elif str[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        sign = 1
    else:
        return 0
    result = 0
    while i < size and str[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        result = 10 * result + int(str[i])
        i += 1
    r = sign * result
    if r > 2147483647:
        return 2147483647
    elif r < -2147483648:
        return -2147483648
    else:
        return r

if __name__ == '__main__':
    print atoi('+12a000')
