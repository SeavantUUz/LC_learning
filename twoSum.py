# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/6'


def twoSum0(nums, target):
    for index, num in enumerate(nums):
        delta = target - num
        find_index = bisearch(nums[index+1:], delta)
        if find_index != -1:
            return index + 1, index + find_index + 1 + 1


def bisearch(nums, x):
    def _bisearch(nums, x, index):
        size = len(nums)
        if not size:
            return -1
        middle = size / 2
        if nums[middle] == x:
            return index+middle
        elif nums[middle] > x:
            return _bisearch(nums[:middle], x, index)
        else:
            return _bisearch(nums[middle+1:], x, index+middle+1)
    return _bisearch(nums, x, 0)


def twoSum(nums, target):
    d = dict()
    for i in xrange(len(nums)):
        x = nums[i]
        delta = target - x
        if delta in d:
            return [d[delta]+1, i+1]
        d[x] = i



if __name__ == '__main__':
    # print bisearch([1,2,3,4], 3)
    print twoSum([1,2, 5, 7, 11, 15], 9)
