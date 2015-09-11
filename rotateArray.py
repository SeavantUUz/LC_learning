# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/12'


def rotate(nums, k):
    def swap(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    length = len(nums)
    line = length - k
    if line < 0:
        line = line + length
    swap(0, line - 1)
    swap(line, length-1)
    swap(0, length - 1)



if __name__ == '__main__':
    rotate([1,2,3,4,5,6], 11)