# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/13'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def levelOrderBottom(root):
    result = []
    def one_level(root, level):
        if not root:
            return
        if len(result) == level:
            result.append([])
        level_container = result[level]
        level_container.append(root.val)
        one_level(root.left, level+1)
        one_level(root.right, level+1)
    one_level(root, 0)
    result.reverse()
    return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print levelOrderBottom(root)
