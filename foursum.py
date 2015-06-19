# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/19'

def fourSum(nums, target):
    nums.sort()
    duplication = dict()
    result = []
    def twoSum(start, end, target):
        i = start + 1
        j = end - 1
        sub_target = target - (nums[start] + nums[end])
        while i < j:
            array = (nums[start], nums[i], nums[j], nums[end])
            if nums[i] + nums[j] == sub_target and array not in duplication:
                result.append(array)
                duplication[array] = 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < sub_target:
                i += 1
            else:
                j -= 1
    size = len(nums)
    start = 0
    end = size - 1
    while start < end:
        if nums[start] > target / 4:
            break
        j = end
        while start + 2 < j:
            if nums[j] < target / 4:
                break
            twoSum(start, j, target)
            j -= 1
        start += 1
    return result


if __name__ == '__main__':
    print fourSum([-3,-1,0,2,4,5], 1)

