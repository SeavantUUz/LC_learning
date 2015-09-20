# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/20'


def findRepeatedDnaSequences(s):
    r_dict = dict()
    length = len(s)
    if length < 10:
        return []
    for i in xrange(0, length - 10 + 1):
        r = s[i:i+10]
        r_dict.setdefault(r, []).append(1)
    result = []
    for r in r_dict:
        if sum(r_dict[r]) > 1:
            result.append(r)
    return result


if __name__ == '__main__':
    print findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")