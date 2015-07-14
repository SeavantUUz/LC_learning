# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/14'


def lengthOfLastWord(s):
    size = len(s)
    index = size - 1
    while index >= 0:
        if s[index] == ' ':
            index -= 1
        else:
            break
    if index == -1:
        return 0
    count = 0
    while index >= 0:
        if s[index] == ' ':
            break
        else:
            count += 1
            index -= 1
    return count


if __name__ == '__main__':
    print lengthOfLastWord('a ')
