# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/2'


def numDecodings0(s):
    if not s:
        return 0
    count = 1
    prep = int(s[0])
    for num_str in s[1:]:
        count += 1
        num = int(num_str)
        if prep * 10 + num < 27:
            count += 1
        prep = num
    return count


def numDecodings1(s):
    if not s:
        return 0
    if len(s) == 1:
        if int(s[0]):
            return 1
        else:
            return 0
    if s[0] == '0' and s[1] == '0':
        n = [0, 0]
    elif s[0] == '0':
        n = [0, 1]
    elif s[1] =='0':
        n = [1, 1]
    elif int(s[:2]) > 26:
        n = [1, 1]
    else:
        n = [1, 2]
    prep = int(s[1])
    index = 1
    for num_str in s[2:]:
        num = int(num_str)
        if 0 < prep * 10 + num < 27 and prep != 0 and num !=0:
            value = n[index-1] + n[index-2]
        else:
            value = n[index-1]
        prep = num
        n.append(value)
    return n[-1]


def numDecodings(s):
    if not s:
        return 0
    length = len(s)
    n = [0] * (length + 1)
    n[0] = 1
    for i in xrange(length):
        if int(s[i]) != 0:
            n[i+1] = n[i]
        if i>0 and 10 <= int(s[i-1:i+1]) <= 26:
            n[i+1] += n[i-1]
    return n[-1]

if __name__ == '__main__':
    print numDecodings('01')

