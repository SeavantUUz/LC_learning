# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/8'


def permute(nums):
    size = len(nums)
    if size < 2:
        return [nums]
    dup_dict = dict()

    def reverse(_nums, start, end):
        while start < end:
            _nums[start], _nums[end] = _nums[end], _nums[start]
            start += 1
            end -= 1
        return _nums

    def get_next_permute(nums):
        index = size - 2
        k = -1
        while index >= 0:
            if nums[index] < nums[index+1]:
                k = index
                break
            else:
                index -= 1
        if k == -1:
            return reverse(nums, 0, size-1)
        index = size - 1
        l = -1
        while index > k:
            if nums[index] > nums[k]:
                l = index
                break
            else:
                index -= 1
        nums[l], nums[k] = nums[k], nums[l]
        return reverse(nums, k+1, size-1)

    result = [nums]
    dup_dict[tuple(nums)] = 1
    while True:
        nums = get_next_permute(nums)
        t = tuple(nums)
        if dup_dict.get(t):
            continue
        else:
            dup_dict[t] = 1
            result.append(nums[:])
    return result

if __name__ == '__main__':
    print permute([1,2,3,4])

