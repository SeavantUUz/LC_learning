# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/8'


def majorityElement0(nums):
    nums.sort()
    return nums[len(nums) / 2]


def majorityElement(nums):
    cur, c = 0, 0
    for num in nums:
        if c == 0:
            cur, c = num, 1
        elif cur == num:
            c += 1
        else:
            c-=1
    return cur


if __name__ == '__main__':
    print majorityElement([2,1,2])
