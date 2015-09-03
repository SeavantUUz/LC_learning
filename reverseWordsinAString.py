# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/2'


def reverseWords(s):
    if not s:
        return s
    words = s.split()
    length = len(words)
    left = 0
    right = length - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return ' '.join(words)

if __name__ == '__main__':
    print reverseWords( "the sky is blue")
