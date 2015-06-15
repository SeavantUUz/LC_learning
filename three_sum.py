# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/15'

def three_sum(nums):
    nums.sort()
    size = len(nums)
    solutions = []
    record = dict()
    for i, num in enumerate(nums):
        if num in record:
            continue
        if num > 0:
            break
        record[num] = 1
        result = -num
        r_dict = dict()
        dup = dict()
        for j in xrange(i+1, size):
            if nums[j] in r_dict and nums[j] not in dup:
                solutions.append([num, r_dict[nums[j]], nums[j]])
                dup[nums[j]] = 1
            target = result - nums[j]
            r_dict[target] = nums[j]
    return solutions


if __name__ == '__main__':
    print three_sum([0,0,0])




