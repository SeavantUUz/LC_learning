# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/27'


def singleNumber(nums):
    nums.sort()
    length = len(nums)
    index = 0
    while index < length-1:
        if nums[index+1] - nums[index] == 0:
            index += 2
        else:
            r = index
            break
    else:
        r = length - 1
    return nums[r]


if __name__ == '__main__':
    print singleNumber([1,1,2])
