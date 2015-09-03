# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/3'


# 这个方法真是好有道理……
def maxProduct(nums):
    cur_max = cur_min = nums[0]
    ans = nums[0]
    for num in nums[1:]:
        values = [num, cur_max*num, cur_min*num]
        cur_max = max(values)
        cur_min = min(values)
        ans = max(cur_max, ans)
    return ans


if __name__ == '__main__':
    print maxProduct([2,3,-2,4])

