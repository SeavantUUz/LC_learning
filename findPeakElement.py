# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/6'


def findPeakElement(nums):
    index = 1
    nums.insert(0, float('-inf'))
    nums.append(float('-inf'))
    for element in nums[1:-1]:
        if element > nums[index-1] and element > nums[index+1]:
            return index-1
        else:
            index += 1

if __name__ == '__main__':
    print findPeakElement([1])