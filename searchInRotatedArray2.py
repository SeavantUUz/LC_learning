# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/20'


def search(nums, target):
    if not nums:
        return False
    def bisearch(nums, target):
        print nums
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = left+(right-left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return -1
    length = len(nums)
    pivot = 0
    for i in xrange(1, length):
        if nums[i-1] > nums[i]:
            pivot = i
            break
    index = bisearch(nums[:pivot], target)
    if index != -1:
        return True
    else:
        index = bisearch(nums[pivot:], target)
        if index != -1:
            return True
        else:
            return False


if __name__ == '__main__':
    print search([3,5,1], 3)