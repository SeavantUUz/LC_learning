# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/3'


def findMin(nums):
    first = nums[0]
    for num in nums[1:]:
        if num < first:
            break
    else:
        return first
    return num


if __name__ == '__main__':
    print findMin([4,5,6,7,0,1,2])
