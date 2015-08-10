# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/10'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def zigzagLevelOrder(root):
    result = []
    def each_level(root, level, direction):
        if root is None:
            return
        if len(result) == level:
            result.append([])
        if direction == 'left':
            result[level].append(root.val)
            each_level(root.left, level+1, 'right')
            each_level(root.right, level+1, 'right')
        else:
            result[level].insert(0, root.val)
            each_level(root.left, level+1, 'left')
            each_level(root.right, level+1, 'left')
    each_level(root, 0, 'left')
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print zigzagLevelOrder(root)