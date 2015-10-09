# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/9'


def summaryRanges(nums):
    result = []
    if not nums:
        return []
    length = len(nums)
    if length == 1:
        return [str(nums[0])]
    last_start = nums[0]
    last_end = nums[0]
    nums += [-1]
    for num in nums[1:]:
        if num == last_end + 1:
            last_end = num
        else:
            if last_start == last_end:
                result.append(str(last_end))
            else:
                result.append('{}->{}'.format(last_start, last_end))
            last_start = num
            last_end = num
    return result


if __name__ == '__main__':
    print summaryRanges([1, 3])

