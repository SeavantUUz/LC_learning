# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/27'


# 最简单的方法，整个排序，取倒数第k个
def findKthLargest0(nums, k):
    return sorted(nums)[-k]


def findKthLargest(nums, k):
    def partition(nums, left, right):
        pivot = nums[right]
        i = left
        for j in xrange(left, right):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def quick_select(nums, start, end, k):
        pos = partition(nums, start, end)
        if pos == k-1:
            return nums[pos]
        elif pos > k-1:
            return quick_select(nums, start, pos-1, k)
        return quick_select(nums, pos+1, end, k)

    length = len(nums)
    return quick_select(nums, 0, length-1, k)


if __name__ == '__main__':
    print findKthLargest([3,2,1,5,6,4], 5)
