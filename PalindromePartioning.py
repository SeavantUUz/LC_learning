# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/24'


def partition0(s):
    palindrome_memo = dict()
    result = []
    length = len(s)
    if not s:
        return []
    if length == 1:
        return [s]
    def is_palindrome(string):
        if string in palindrome_memo:
            return palindrome_memo[string]
        length = len(string)
        left = 0
        right = length - 1
        while left < right:
            if string[left] != string[right]:
                palindrome_memo[string] = False
                break
            else:
                left += 1
                right -= 1
        else:
            palindrome_memo[string] = True
            return True
        return False

    def partition_helper(one_solution, start, end):
        if start >= length:
            return
        if end >= length:
            solution = one_solution+[s[start:]]
            for word in solution:
                if not is_palindrome(word):
                    return
            else:
                result.append(solution)
                return
        t = s[start:end]
        partition_helper(one_solution, start, end+1)
        partition_helper(one_solution+[t], end, end+1)
    partition_helper([], 0, 1)
    return result


def partition(s):
    palindrome_memo = dict()
    length = len(s)
    if not s:
        return []
    if length == 1:
        return [[s]]
    def is_palindrome(string):
        if string in palindrome_memo:
            return palindrome_memo[string]
        length = len(string)
        left = 0
        right = length - 1
        while left < right:
            if string[left] != string[right]:
                palindrome_memo[string] = False
                break
            else:
                left += 1
                right -= 1
        else:
            palindrome_memo[string] = True
            return True
        return False
    def partition_helper(string):
        result = []
        for i in xrange(1, len(string)):
            if is_palindrome(string[:i]):
                head = string[:i]
                rest = string[i:]
                for l in partition_helper(rest):
                    result.append([head]+l)
        if is_palindrome(string):
            result.append([string])
        return result
    return partition_helper(s)


if __name__ == '__main__':
    print partition("a")

