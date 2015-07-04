# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/3'

def searchRange(nums, target):
    left = 0
    size = len(nums)
    right = size - 1
    start = -1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            start = mid
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    left = 0
    right = size - 1
    end = -1
    while left <= right:
        mid = (left + right)
        if nums[mid] == target:
            end = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [start, end]


