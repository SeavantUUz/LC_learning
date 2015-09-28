# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/28'


def containsDuplicate(nums):
    dup = dict()
    for num in nums:
        if num in dup:
            break
        dup[num] = 1
    else:
        return False
    return True