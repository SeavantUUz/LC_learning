# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/15'



def permutationSequence0(n, k):
    index = 1
    candidate = []
    while index <= n:
        candidate.append(index)
        index += 1
    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def get_next_permutation(nums):
        k = -1
        size = len(nums)
        if size < 2:
            return nums
        index = size - 2
        while index >= 0:
            if nums[index] < nums[index + 1]:
                k = index
                break
            else:
                index -= 1
        if k == -1:
            return reverse(nums, 0, size-1)
        l = -1
        index = size - 1
        while index >= k:
            if nums[index] > nums[k]:
                l = index
                break
            else:
                index -= 1
        nums[k], nums[l] = nums[l], nums[k]
        return reverse(nums, k+1, size - 1)
    k -= 1
    while k > 0:
        candidate = get_next_permutation(candidate)
        k -= 1
    return ''.join(map(str, candidate))


def permutationSequence(n, k):
    memo = dict()
    def fact(n):
        if memo.get(n):
            return memo[n]
        elif n==0:
            return 1
        else:
            result = n * fact(n-1)
            memo[n] = result
            return result
    candidate = range(1, n+1)
    result = []
    level = n
    k -= 1
    while k>0 and level > 1:
        factorial = fact(level-1)
        index = k / factorial
        result.append(candidate[index])
        candidate.remove(candidate[index])
        k = k % factorial
        level -= 1
    result.extend(candidate)
    return ''.join(map(str, result))


# 783269514
if __name__ == '__main__':
    print permutationSequence0(1, 1)
    print permutationSequence(1, 1)
