# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/14'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


def isBalance(root):
    def depth(root):
        if not root:
            return 0
        else:
            left_depth = depth(root.left)
            if left_depth == -1:
                return -1
            right_depth = depth(root.right)
            if right_depth == -1:
                return -1
            if not abs(left_depth-right_depth) > 1:
                return 1+max(left_depth, right_depth)
            else:
                return -1
    return depth(root) != -1


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(20)
    print isBalance(root)
