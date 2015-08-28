# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/28'


def wordBreak0(s, wordDict):
    memo = dict()
    def helper(s):
        length = len(s)
        if length == 0:
            return True
        results = []
        for i in xrange(length+1):
            if s[:i] in memo:
                if memo[s[:i]]:
                    results.append(helper(s[i:]))
            else:
                if s[:i] in wordDict:
                    results.append(helper(s[i:]))
                    memo[s[:i]] = True
                else:
                    memo[s[:i]] = False
        return any(results)
    if not s:
        return False
    return helper(s)


def wordBreak(s, wordDict):
    length = len(s)
    dp = [False] * (length+1)
    dp[0] = True
    for i in xrange(1, length+1):
        for j in xrange(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]


if __name__ == '__main__':
    # s = 'aaaaaaa'
    # word_dict = ['aaaa', 'aa']
    s = 'leetcode'
    word_dict = ['leet', 'code']
    print wordBreak(s, word_dict)
