# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/5'


def combinationSum(candidates, target):
    solutions = []
    solution_dict = dict()
    candidates = list(candidates)
    candidates.sort()

    def one_solution(candidates, solution, remain):
        if remain == 0:
            sol = tuple(solution)
            if not solution_dict.get(sol):
                solutions.append(solution[:])
                solution_dict[sol] = 1
            return
        if not candidates:
            return
        if remain - candidates[0] < 0:
            return
        first = candidates[0]
        one_solution(candidates[1:], solution, remain)
        solution.append(first)
        one_solution(candidates, solution, remain - first)
        solution.pop()

    one_solution(candidates, [], target)
    return solutions


if __name__ == '__main__':
    print combinationSum({2, 3, 6, 7}, 7)
