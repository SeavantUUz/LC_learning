# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/15'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


def pathSum(root, sum):
    solutions = []
    def one_solution(root, solution, remain):
        if not root:
            return
        left = root.left
        right = root.right
        if not left and not right:
            if root.val == remain:
                solution.append(root)
                solutions.append(solution[:])
                return
            else:
                return
        else:
            one_solution(root.left, solution+[root], remain-root.val)
            one_solution(root.right, solution+[root], remain-root.val)
    one_solution(root, [], sum)
    return True if len(solutions) >= 1 else False


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    a = pathSum(root, 22)
    print [str(node) for node in a[0]]

