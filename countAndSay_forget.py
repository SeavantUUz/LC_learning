# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/5'

def countAndSay(n):
    result = []
    count = 1
    pre = n % 10
    num = pre
    n = n / 10
    if n == 0:
        return str(10+pre)
    while n > 0:
        num = n % 10
        if num == pre:
            count += 1
        else:
            r = 10*count + pre
            result.insert(0, str(r))
            pre = num
            count = 1
        n = n/10
    result.insert(0, str(10*count + num))
    return ''.join(result)


if __name__ == '__main__':
    print countAndSay(1211)