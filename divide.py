# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/29'

def divide(dividend, divisor):
    sign = 1
    if dividend < 0:
        sign = -1
        dividend = 0 - dividend
    if divisor < 0:
        if sign == -1:
            sign = 1
        else:
            sign = -1
        divisor = 0 - divisor
    if dividend == 0:
        return 0
    remain = dividend
    count = 0
    while divisor <= remain:
        d = divisor
        local_count = 1
        while remain - d >= d:
            d += d
            local_count += local_count
        remain = remain - d
        count += local_count
    if sign == -1:
        count = 0 - count
    if count > 2147483647:
        return 2147483647
    elif count < -2147483648:
        return -2147483648
    else:
        return count


if __name__ == '__main__':
    print divide(10, 2)



