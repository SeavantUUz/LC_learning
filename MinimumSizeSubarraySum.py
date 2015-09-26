# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/25'

def minSubArrayLen(s, nums):
    length = len(nums)
    left = 0
    right = 0
    min_length = 0
    sum = 0
    while right < length:
        sum += nums[right]
        while sum >= s:
            l = right - left + 1
            if min_length == 0:
                min_length = l
            else:
                if l < min_length:
                    min_length = l
            sum -= nums[left]
            left += 1
        right += 1
    return min_length


if __name__ == '__main__':
    print minSubArrayLen(7, [2,3,1,2,4,3])
