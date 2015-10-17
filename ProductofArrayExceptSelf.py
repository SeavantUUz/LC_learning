# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/17'


def productExceptSelf(nums):
    length = len(nums)
    left = [1] * length
    index = 1
    last_product = nums[0]
    while index < length:
        left[index] = last_product
        last_product *= nums[index]
        index += 1
    right = [1] * length
    last_product = nums[-1]
    index = length - 2
    while index >= 0:
        right[index] = last_product
        last_product *= nums[index]
        index -= 1
    index = 0
    while index < length:
        nums[index] = left[index] * right[index]
        index += 1
    return nums


if __name__ == "__main__":
    # print productExceptSelf([1,2,3,4])
    print productExceptSelf([0,0])
