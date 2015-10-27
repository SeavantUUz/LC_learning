# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/27'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        length = len(nums)
        count = 0
        while i < length:
            if nums[i] == 0:
                i += 1
                count += 1
            else:
                nums[j] = nums[i]
                j += 1
                i += 1
        while j < length:
            nums[j] = 0
            j += 1


if __name__ == '__main__':
    s = Solution()
    print s.moveZeroes([0, 1, 0, 3, 12])