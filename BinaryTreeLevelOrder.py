# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/9'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def levelOrder(root):
    result = []
    def each_level(root, level):
        if root is None:
            return
        if len(result) == level:
            result.append([])
        result[level].append(root.val)
        each_level(root.left, level+1)
        each_level(root.right, level+1)
    each_level(root, 0)
    return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print levelOrder(root)
