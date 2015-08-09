# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/8'


def isSymmetric(root):
    def check_tree(node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return check_tree(node1.left, node2.right) and check_tree(node1.right, node2.left)
    if root is None:
        return True
    return check_tree(root.left, root.right)

