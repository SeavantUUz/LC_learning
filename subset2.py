# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/2'


def subsetsWithDup(nums):
    result = []
    length = len(nums)
    dup_dict = dict()
    if not nums:
        return nums
    nums.sort()
    def one_solution(solution, index):
        if index >= length:
            t = tuple(solution)
            if t in dup_dict:
                return
            else:
                dup_dict[t] = 1
                result.append(solution[:])
                return
        else:
            one_solution(solution, index + 1)
            solution.append(nums[index])
            one_solution(solution, index + 1)
            solution.pop()
    one_solution([], 0)
    return result


if __name__ == '__main__':
    print subsetsWithDup([1,2,2])
