# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/7'


def lengthOfLongestSubstring0(s):
    char_dict = dict()
    size = len(s)
    def dp(index, pos):
        if index == size:
            return 0
        first = s[index]
        if first not in char_dict:
            char_dict[first] = index
            return max(pos+1, dp(index+1, pos+1))
        else:
            old_index = char_dict[first]
            char_dict[first] = index
            return max(index-old_index, dp(index+1, 0))
    return dp(0, 0)


def lengthOfLongestSubstring(s):
    char_dict = dict()
    max_length = last_max_length = 0
    start = 0
    for index in xrange(len(s)):
        char = s[index]
        if char not in char_dict or char_dict[char]< start:
            max_length += 1
            char_dict[char] = index
        else:
            if max_length > last_max_length:
                last_max_length = max_length
            max_length = index - char_dict[char]
            start = char_dict[char] + 1
            char_dict[char] = index
    if last_max_length < max_length:
        last_max_length = max_length
    return last_max_length


if __name__ == '__main__':
    print lengthOfLongestSubstring("abcabc")
