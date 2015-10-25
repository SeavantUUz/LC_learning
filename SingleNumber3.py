# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/25'

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r_dict = dict()
        r_list = []
        for num in nums:
            if num in r_dict:
                r_dict[num] += 1
            else:
                r_dict[num] = 1
        for num in r_dict:
            if r_dict[num] == 1:
                r_list.append(num)
        return r_list

