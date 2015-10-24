# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/23'


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        a = set(range(length+1))
        return list((a - set(nums)))[0]


if __name__ == '__main__':
    s = Solution()
    print s.missingNumber([0,1,3])