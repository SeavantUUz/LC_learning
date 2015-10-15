# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/14'


def lowestCommonAncestor(root, p, q):
    lower, higher = sorted([p.val, q.val])
    while root:
        if not root:
            return None
        val = root.val
        if val == higher or val == lower or (val > lower and val < higher):
            return root
        elif val > higher:
            root = root.left
        else:
            root = root.right
    else:
        return None

