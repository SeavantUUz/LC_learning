# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/30'


def containsNearbyDuplicate(self, nums, k):
    dup = dict()
    for index, num in enumerate(nums):
        if num in dup:
            values = dup[num]
            for value in values:
                if abs(index - value) <= k:
                    return True
            else:
                dup[num].append(index)
        else:
            dup.setdefault(num, []).append(index)
    else:
        return False