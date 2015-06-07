# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/4'

def subsets1(nums):
    result = []
    if not nums:
        return tuple()
    for i in xrange(len(nums)):
        left = nums[:i]
        right = nums[i+1:]
        result.append(tuple(left+right))
        result.extend(subsets1(left+right))
    return result

def subsets2(nums):
    result = []
    result.append([])
    for i, element in enumerate(nums):
        right = nums[i+1:]
        result.append([element])
        if right:
            for left_index in xrange(len(right)):
                for right_index in xrange(1, len(right) + 1):
                    if left_index != right_index:
                        part = right[left_index:right_index]
                        t_l = [element]
                        t_l.extend(part)
                        result.append(t_l)
    return result


def subsets3(nums):
    result = []
    size = len(nums)
    def dfs(depth, start, value_list):
        result.append(value_list)
        if depth == size: return
        for i in range(start, size):
            value = nums[i]
            dfs(depth + 1, i + 1, value_list + [value])
    dfs(0, 0, [])
    return result


def subsets4(nums):
    result = []
    size = len(nums)
    def rec(index, temp, result):
        if index == size:
            result.append(temp)
        else:
            rec(index + 1, temp, result)
            temp.append(nums[index])
            rec(index + 1, temp, result)
            temp.pop()
    rec(0, [], result)
    return result



if __name__ == '__main__':
    # print [list(tp) for tp in set(subsets([1,2,3]))]
    print subsets4([1,2,3,4])