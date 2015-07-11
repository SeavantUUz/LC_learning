# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/3'

def permutations(nums):
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    size = len(nums)
    if size < 2:
        return
    index = size-2
    k = -1
    while index >= 0:
        if nums[index] < nums[index+1]:
            k = index
            break
        else:
            index -= 1
    if k == -1:
        reverse(0, size-1)
        return
    index = size - 1
    l = -1
    while index > k:
        if nums[index] > nums[k]:
            l = index
            break
        else:
            index -= 1
    nums[k], nums[l] = nums[l], nums[k]
    reverse(k+1, size-1)

if __name__ == '__main__':
    permutations([1, 2, 3, 5])
