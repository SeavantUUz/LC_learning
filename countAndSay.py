# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/5'


def countAndSay(n):
    def read_it(now):
        result = []
        pre = ''
        count = 1
        cur = ''
        for char in now:
            cur = char
            if not pre:
                pre = char
                count = 1
            elif char == pre:
                count += 1
            else:
                result.append(str(count) + pre)
                pre = char
                count = 1
        result.append(str(count) + cur)
        return ''.join(result)
    now = "1"
    n -= 1
    while n > 0:
        now = read_it(now)
        n -= 1
    return now


if __name__ == '__main__':
    print countAndSay(5)
