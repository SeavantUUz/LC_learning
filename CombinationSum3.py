# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/27'


# 这个是包含重复值的情况，看起来，题意要求没有重复值，我很不解，这样简单不少
# 而且，这样其实只有9!个枚举值，实在不大，当然，带剪枝的dp更快
def combinationSum3(k, n):
    solutions = []
    dup = dict()
    candidates = range(1, 10)
    def helper(one_solution, candidate, delta, level):
        if level == k:
            if delta == 0:
                t = tuple(one_solution)
                if t not in dup:
                    solutions.append(one_solution[:])
                    dup[t] = 1
            return
        if not candidate or level > k or delta < candidate[0]:
            return
        else:
            i = candidate[0]
            helper(one_solution+[i], candidate[1:], delta - i, level+1)
            helper(one_solution, candidate[1:], delta, level)
    helper([],candidates, n, 0)
    return solutions


if __name__ == '__main__':
    print combinationSum3(3, 15)


