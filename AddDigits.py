# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/20'

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num-1) % 9 + 1
