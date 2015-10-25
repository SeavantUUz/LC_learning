# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/25'


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left < right:
            mid = ((right - left) >> 1) + left
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right