# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/19'


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d1 = dict()
        d2 = dict()
        pattern_length = len(pattern)
        ss = str.split()
        if pattern_length != len(ss):
            return False
        for p, s in zip(list(pattern), str.split()):
            if p in d1 and d1[p] != s:
                return False
            elif s in d2 and d2[s] != p:
                return False
            else:
                if p not in d1:
                    d1[p] = s
                    d2[s] = p
        return True


if __name__ == '__main__':
    s = Solution()
    print s.wordPattern('abba', "dog dog dog fish")