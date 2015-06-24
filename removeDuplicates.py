# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/24'

def removeDuplicates(nums):
    size = len(nums)
    if size < 2:
        return size
    postNum = nums[-1]
    index = size-2
    count = 1
    while index >= 0:
        currentNum = nums[index]
        if not currentNum == postNum:
            count += 1
            postNum = currentNum
        else:
            del nums[index]
        index -= 1
    return count


if __name__ == '__main__':
    print removeDuplicates([1,1])

