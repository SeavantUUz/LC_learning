# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/17'


def getRow(rowIndex):
    result = [1]
    for i in xrange(rowIndex):
        result.insert(0, 0)
        result.append(0)
        for j in xrange(i+1):
            result[j] = result[j] + result[j+1]
        result.pop()
    return result


if __name__ == '__main__':
    print getRow(2)

