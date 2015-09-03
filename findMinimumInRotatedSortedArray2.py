# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/3'


# 毫无影响，因为是单调的
def findMin(nums):
    first = nums[0]
    for num in nums[1:]:
        if num < first:
            break
    else:
        return first
    return num