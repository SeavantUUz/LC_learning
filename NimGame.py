# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/19'


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4:
            return True
        else:
            return False