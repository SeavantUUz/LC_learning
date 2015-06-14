# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/14'


def longestCommonPrefix(strs):
    def is_common_prefix(endpoint, prefix):
        for str in strs:
            if str[:endpoint] != prefix:
                return False
        else:
            return True
    shortest_string = ''
    shortest_string_length = 65535
    for str in strs:
        length = len(str)
        if length < shortest_string_length:
            shortest_string = str
            shortest_string_length = length
    left = 0
    right = shortest_string_length - 1
    while left <= right:
        mid = (left + right) / 2
        if is_common_prefix(mid+1, shortest_string[:mid+1]):
            left = mid + 1
        else:
            right = mid - 1
    mid = (left + right) / 2
    return shortest_string[:mid+1]


if __name__ == '__main__':
    print longestCommonPrefix(["a","aba","abc"])
