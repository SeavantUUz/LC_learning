# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/5'


def invertBinaryTree(root):
    if not root:
        return None
    def invert(root):
        if not root:
            return None
        root.right, root.left = root.left, root.right
        invert(root.right)
        invert(root.left)
    invert(root)
    return root


if __name__ == '__main__':
    pass
