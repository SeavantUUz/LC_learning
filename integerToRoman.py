# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/14'

def integerToRoman(num):
    # mapping = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
    # for group in mapping:
    result = ''
    t = num / 1000
    result += 'M'*t
    num -= t*1000
    h = num /100
    if h in [9]:
        result += 'CM'
    elif h in [8, 7, 6]:
        result += 'D' + 'C' * (h-5)
    elif h in [5, 4]:
        result += 'C'*(5-h) + 'D'
    elif h in [1, 2, 3]:
        result += 'C' * h
    num -= h*100
    h = num / 10
    if h in [9]:
        result += 'XC'
    elif h in [8, 7, 6]:
        result += 'L' + 'X' * (h-5)
    elif h in [5, 4]:
        result += 'X'*(5-h) + 'L'
    elif h in [1, 2, 3]:
        result += 'X' * h
    num -= h*10
    h = num
    if h in [9]:
        result += 'IX'
    elif h in [8, 7, 6]:
        result += 'V' + 'I' * (h-5)
    elif h in [5, 4]:
        result += 'I'*(5-h) + 'V'
    elif h in [1, 2, 3]:
        result += 'I' * h
    return result


if __name__ == '__main__':
    print integerToRoman(110)

