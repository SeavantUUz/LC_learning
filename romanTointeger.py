# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/14'


def romanToInteger(s):
    mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    size = len(s)
    index = size - 1
    result = 0
    while index >= 0:
        current = s[index]
        current_value = mapping[current]
        pre = index - 1
        if pre >= 0:
            pre_char = s[pre]
            pre_char_value = mapping[pre_char]
            if pre_char_value < current_value:
                result += current_value - pre_char_value
                index = pre
            else:
                result += current_value
        else:
            result += current_value
        index -= 1
    return result


if __name__ == '__main__':
    print romanToInteger('XLV')



