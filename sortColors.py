# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/23'


def sortColors0(nums):
    if not nums:
        return nums
    red = 0
    white = 0
    blue = 0
    for i in nums:
        if i == 0:
            red += 1
        elif i==1:
            white += 1
        else:
            blue += 1
    index = 0
    while red > 0:
        nums[index] = 0
        index += 1
        red -= 1
    while white > 0:
        nums[index] = 1
        index += 1
        white -= 1
    while blue > 0:
        nums[index] = 2
        index += 1
        blue -= 1
    print nums


def sortColors(nums):
    if not nums:
        return nums
    n = len(nums)
    first_pointer = 0
    second_pointer = n - 1
    index = 0
    while index <= second_pointer:
        if nums[index] == 0:
            nums[index], nums[first_pointer] = nums[first_pointer], nums[index]
            first_pointer += 1
            index += 1
        elif nums[index] == 2:
            nums[index], nums[second_pointer] = nums[second_pointer], nums[index]
            second_pointer -= 1
        else:
            index += 1
    print nums



if __name__ == '__main__':
    sortColors([1,0,0,2,1,2,0,1])




