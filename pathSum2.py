# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/15'


def pathSum(root, sum):
    solutions = []
    def one_solution(root, solution, remain):
        if not root:
            return
        left = root.left
        right = root.right
        if not left and not right and root.val == remain:
            solution.append(root.val)
            solutions.append(solution)
        one_solution(root.left, solution+[root.val], remain-root.val)
        one_solution(root.right, solution+[root.val], remain-root.val)
    one_solution(root, [], sum)
    return solutions