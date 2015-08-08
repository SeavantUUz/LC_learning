# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/8'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def isValidBST0(root):
    if not root:
        return True
    def isValidTree(root, value, flag):
        if not root:
            return True
        left = root.left
        right = root.right
        if flag == 'left':
            if left and left.val >= value:
                return False
            if right and right.val >= value:
                return False
        else:
            if left and left.val <= value:
                return False
            if right and right.val <= value:
                return False
        if left:
            if left.val >= root.val:
                return False
        if right:
            if right.val <= root.val:
                return False
        return isValidTree(left, root.val, 'left') and isValidTree(right, root.val, 'right')
    left = root.left
    right = root.right
    if left:
        if left.val >= root.val:
            return False
    if right:
        if right.val <= root.val:
            return False
    return isValidTree(left, root.val, 'left') and isValidTree(right, root.val, 'right')


def isValidBST(root):
    def isValidTree(root, min, max):
        if not root:
            return True
        else:
            if root.val >= max or root.val <= min:
                return False
            return isValidTree(root.left, min, root.val) and isValidTree(root.right, root.val, max)
    return isValidTree(root, float('-inf'), float('inf'))



if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(20)
    print isValidBST(root)
