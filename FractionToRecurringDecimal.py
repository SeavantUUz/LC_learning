# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/6'


def fractionToDecimal(numerator, denominator):
    flag = 1
    if numerator < 0:
        numerator = -numerator
        flag *= -1
    if denominator < 0:
        denominator = -denominator
        flag *= -1
    result = []
    dup_list = []
    integer = numerator / denominator
    dup = dict()
    remain = numerator % denominator
    if not remain:
        r = str(integer)
        if flag == -1 and r != '0':
            r = '-' + r
        return r
    while remain:
        if remain in dup:
            start_index = dup_list.index(remain)
            break
        else:
            dup[remain] = 1
            dup_list.append(remain)
        remain *= 10
        value = str(remain / denominator)
        remain = remain % denominator
        result.append(value)
    else:
        r = '{}.{}'.format(integer, ''.join(result))
        if flag == -1:
            r = '-'+r
        return r
    if start_index == 0:
        r = '{}.({})'.format(integer, ''.join(result))
    else:
        r = '{}.{}({})'.format(integer, ''.join(result[:start_index]), ''.join(result[start_index:]))
    if flag == -1:
        r = '-'+r
    return r


if __name__ == '__main__':
    print fractionToDecimal(2, 1)
    print fractionToDecimal(1, 2)
    print fractionToDecimal(20, 7)
    print fractionToDecimal(1, 6)
    print fractionToDecimal(50, 8)
    print fractionToDecimal(-50, 8)
    print fractionToDecimal(0, -5)
