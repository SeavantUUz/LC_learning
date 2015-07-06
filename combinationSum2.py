# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/6'

def combinationSum2(candidates, target):
    solutions = []
    solution_dict = dict()
    candidates.sort()

    def one_solution(candidates, solution, remain):
        if remain == 0:
            sol = tuple(solution)
            if not solution_dict.get(sol):
                solutions.append(solution[:])
                solution_dict[sol] = 1
            return
        if not candidates or remain < candidates[0]:
            return
        element = candidates[0]
        one_solution(candidates[1:], solution, remain)
        solution.append(element)
        one_solution(candidates[1:], solution, remain - element)
        solution.pop()

    one_solution(candidates, [], target)
    return solutions


if __name__ == '__main__':
    print combinationSum2([10,1,2,7,6,1,5], 8)