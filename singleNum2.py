# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/27'


def singleNumber(nums):
    nums.sort()
    length = len(nums)
    index = 0
    while index < length:
        if length - 1 - index < 3:
            r = index
            break
        elif nums[index] == nums[index+1] == nums[index+2]:
            index += 3
        else:
            r = index
            break
    return nums[r]


if __name__ == '__main__':
    print singleNumber([1,1,1,2,3,3,3])