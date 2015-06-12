# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/9'


def longestPalindrome0(s):
    size = len(s)
    max_length = 1
    last_string = ''
    last_max_length = 1
    def find_in_substring(pos):
        result = []
        if pos % 2:
            pre = pos - 1
            post = pos + 1
            max_length = 1
            result.append(s[pos])
        else:
            pre = pos
            post = pos + 1
            max_length = 0
        while pre >= 0 and post <= size-1:
            if s[pre] == s[post]:
                max_length += 2
                result.insert(0, s[pre])
                result.append(s[post])
                pre -= 1
                post += 1
            else:
                break
        return ''.join(result), max_length
    for index in xrange(0, size):
        max_string, max_length = find_in_substring(index)
        if max_length > last_max_length:
            last_max_length = max_length
            last_string = max_string
    return last_string


def longestPalindrome(s):
    def preprocess(s):
        return '#'+'#'.join(list(s))+'#'
    if not s:
        return s
    s = preprocess(s)
    id = 1
    mx = 1
    size = len(s)
    s = '${}%'.format(s)
    p = [0] * len(s)
    for i in xrange(1, size):
        j = 2 * id - i
        if mx - i > p[j]:
            p[i] = p[j]
        else:
            p[i] = mx - i
        while(s[i+p[i]] == s[i-p[i]]):
            p[i] += 1
        if i+p[i] > mx:
            mx = i+p[i]
            id = i
    index = 0
    d = 0
    for i, j in enumerate(p):
        if j > d:
            d = j
            index = i
    return s[index-d+1:index+d].replace('#', '')




if __name__ == '__main__':
    print longestPalindrome('b')
