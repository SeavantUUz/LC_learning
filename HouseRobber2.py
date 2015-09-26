# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/26'


def rob(nums):
    def _rob(nums):
        r = [0] * len(nums)
        r[0] = nums[0]
        r[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            r[i] = max(r[i-2] + nums[i], r[i-1])
        return max(r[-1], r[-2])
    if not nums:
        return 0
    if len(nums) <= 3:
        return max(nums)
    return max(_rob(nums[:-1]), _rob(nums[1:]))

if __name__ == '__main__':
    print rob([1,1,1,1])
