# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/11'


def zigzag(s, numRows):
    result = []
    if not s:
        return ''
    if numRows == 1:
        return s
    for i in xrange(numRows):
        result.append('')
    for i in xrange(len(s)):
        n = i/(2 * numRows-2)
        index = i % (2 * numRows - 2)
        if index > numRows - 1:
            index = 2*(numRows - 1) - index
        result[index] = result[index]+(s[i])
    r_s = ''.join(result)
    return r_s


if __name__ == '__main__':
    print zigzag('PAYPALISHIRING', 3)


