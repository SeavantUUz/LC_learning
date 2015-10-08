# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/8'


# 这个讨论太繁杂，基于stack，废弃
# 啊，没有括号，那就简单了
def calculate0(s):
    res, num, sign, stack = 0, 0, 1, []
    s += '+'
    for c in s:
        if c == ' ':
            continue
        elif c.isdigit():
            num = 10 * num + int(c)
        elif c in ('*', '/'):
            if stack:
                symbol, pre_num = stack.pop()
                if symbol == '*':
                    num = pre_num * num
                else:
                    num = pre_num / num
            stack.append((c, num,))
            num = 0
        elif c in ('+', '-'):
            if stack:
                symbol, pre_num = stack.pop()
                if symbol == '*':
                    num = pre_num * num
                else:
                    num = pre_num / num
            res += sign * num
            num = 0
            if c == '+':
                sign = 1
            else:
                sign = -1
    return res


if __name__ == '__main__':
    print calculate0('3+5/2*2/5-4*2')
