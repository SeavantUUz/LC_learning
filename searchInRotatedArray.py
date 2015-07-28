# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/27'


def search(nums, target):
    length = len(nums)
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            if nums[left] <= target or nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[left] > target or nums[mid] >= nums[left] :
                left = mid + 1
            else:
                right = mid - 1
    return -1
