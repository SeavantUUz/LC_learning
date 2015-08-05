# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/6'


def inorderTraversal0(root):
    result = []
    def traversal(root):
        if root:
            traversal(root.left)
            result.append(root.value)
            traversal(root.right)
        else:
            return
        traversal(root)
    return result


def inorderTraversal(root):
    result = []
    stack = []
    t = root
    while True:
        if t is None:
            try:
                t = stack.pop()
            except Exception:
                break
            result.append(t.val)
            t = t.right
        elif t.left:
            stack.append(t)
            t = t.left
        else:
            result.append(t.val)
            t = t.right
    return result

