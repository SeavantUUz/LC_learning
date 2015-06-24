# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/25'


def removeElement(nums, value):
    size = len(nums)
    if not nums:
        return 0
    count = 0
    index = size - 1
    while index >= 0:
        currentNum = nums[index]
        if currentNum == value:
            del nums[index]
        else:
            count += 1
        index -= 1
    return count


if __name__ == '__main__':
    print removeElement([1,1,1], 1)