# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/8'


def sameTree(self, p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        if not p.val == q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
