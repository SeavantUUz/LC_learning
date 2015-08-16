# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/16'


def generate(numRows):
    result = []
    if not numRows:
        return []
    result.append([1])
    for i in xrange(1, numRows):
        one_level = []
        for j in xrange(i+1):
            level = result[i-1]
            if j == 0 or j == i:
                r = 1
            else:
                r = level[j-1] + level[j]
            one_level.append(r)
        result.append(one_level)
    return result


if __name__ == '__main__':
    print generate(3)
