# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/4'


def searchInsertPosition(nums, target):
    size = len(nums)
    left = 0
    right = size - 1
    mid = 0
    while left <= right:
        mid = (left + right) / 2
        if left == right:
            if nums[mid] < target:
                mid = mid + 1
            break
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return mid


if __name__ == '__main__':
    print searchInsertPosition([1], 1)
    print searchInsertPosition([1,3,5,6], 5)
    print searchInsertPosition([1,3,5,6], 2)
    print searchInsertPosition([1,3,5,6], 7)
    print searchInsertPosition([1,3,5,6], 0)
