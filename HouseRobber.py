# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/13'

def rob0(nums):
    length = len(nums)
    result = {'max_sum':  0}
    def dp(one_sum, index):
        if index >= length:
            if one_sum > result['max_sum']:
                result['max_sum'] = one_sum
            return
        dp(one_sum+nums[index], index + 2)
        dp(one_sum, index+1)
    dp(0, 0)
    return result['max_sum']


def rob(nums):
    if not nums:
        return 0
    length = len(nums)
    result = [0] * length
    result[0] = nums[0]
    if length == 1:
        return nums[0]
    elif length == 2:
        return max([nums[0], nums[1]])
    elif length == 3:
        return max([nums[0] + nums[2], nums[1]])
    else:
        result[1] = nums[1]
        result[2] = nums[0] + nums[2]
        index = 3
        while index < length:
            h1 = result[index-2]
            h2 = result[index-3]
            result[index] = max([h1, h2]) + nums[index]
            index += 1
        return max([result[-1], result[-2]])


if __name__ == '__main__':
    # print rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])
    print rob([1,1,2,1])
