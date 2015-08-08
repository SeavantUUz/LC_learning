# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/8'


def numTrees(n):
    memo = dict()
    def tree_count(nums):
        count = 0
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        t = tuple(nums)
        if t in memo:
            return memo[t]
        for i in xrange(len(nums)):
            left_count = tree_count(nums[:i])
            right_count = tree_count(nums[i+1:])
            if left_count and right_count:
                count += left_count * right_count
            elif left_count:
                count += left_count
            else:
                count += right_count
        memo[t] = count
        return count
    nums = range(1, n+1)
    return tree_count(nums)


if __name__ == '__main__':
    print numTrees(22)