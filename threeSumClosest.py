# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/16'

def threeSumClosest(nums, target):
    nums.sort()
    size = len(nums)
    closest = 999999
    result = 0
    for i, num in enumerate(nums):
        remain = target - num
        left = i + 1
        right = size - 1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == remain:
                return target
            elif two_sum < remain:
                left += 1
                delta = remain - two_sum
                if delta < closest:
                    closest = delta
                    result = two_sum + num
            else:
                right -= 1
                delta = two_sum - remain
                if delta < closest:
                    closest = delta
                    result = two_sum + num
    return result


if __name__ == '__main__':
    print threeSumClosest([-1, 2, 1, -4], 1)
    print threeSumClosest([1, 1, 1], 1)


