# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/14'


def canJump(nums):
    m = 0
    size = len(nums)
    i = 0
    while i < size:
        if i > m:
            return False
        m = max(i+nums[i], m)
        i += 1
    return True


if __name__ == '__main__':
    print canJump([3, 2, 1, 0, 4])