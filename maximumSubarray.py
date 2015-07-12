# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/12'


# O(n)
def maximumSubarray0(nums):
    if nums:
        max_value = nums[0]
        current_max_subarray = nums[0]
        for i in xrange(1, len(nums)):
            current_max_subarray = max(nums[i], current_max_subarray + nums[i])
            max_value = max(max_value, current_max_subarray)
        return max_value
    else:
        return 0


def maximumSubarray(nums):
    def find_max_subarray(left, right):
        mid = (left + right) / 2
        if left == right:
            return nums[mid]
        else:
            sub_left = find_max_subarray(left, mid)
            sub_right = find_max_subarray(mid+1, right)
            left_max = nums[mid]
            right_max = nums[mid+1]
            i = mid
            total_num = 0
            while i >= left:
                total_num += nums[i]
                left_max = total_num if total_num > left_max else left_max
                i -= 1
            i = mid + 1
            total_num = 0
            while i <= right:
                total_num += nums[i]
                right_max = total_num if total_num > right_max else right_max
                i += 1
            return max(max(sub_left, sub_right), left_max + right_max)


    if nums:
        left = 0
        right = len(nums) - 1
        return find_max_subarray(left, right)
    else:
        return 0


if __name__ == '__main__':
    print maximumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
