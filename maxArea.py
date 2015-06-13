# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/14'

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return max_area