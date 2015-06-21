# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/22'


def validParentheses(s):
    t = []
    mapping = {'}': '{', ')': '(', ']': '['}
    keys = ['(', '[', '{']
    for c in s:
        if c in keys:
            t.append(c)
        else:
            if t:
                parent = t.pop()
                if parent != mapping[c]:
                    break
            else:
                break
    else:
        if not t:
            return True
        else:
            return False
    return False


if __name__ == '__main__':
    print validParentheses("()[]{")
