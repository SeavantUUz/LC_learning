# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/16'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


def flatten(root):
    def flatten_subtree(root):
        if not root:
            return None
        flatten_subtree(root.left)
        flatten_subtree(root.left)
        flatten_subtree(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
    flatten_subtree(root)




if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    flatten(root)
