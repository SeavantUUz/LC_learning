# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/13'


def isPalindrome(head):
    nums = []
    while head:
        val = head.val
        nums.append(val)
        head = head.next
    length = len(nums)
    left = 0
    right = length - 1
    while left <= right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    else:
        return True