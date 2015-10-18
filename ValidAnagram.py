# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/18'


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = self.helper(s)
        b = self.helper(t)
        return a==b

    def helper(self, s):
        d = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 0
        return d