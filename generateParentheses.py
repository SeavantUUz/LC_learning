# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/22'

def generateParentheses(n):
    result = []
    if not n:
        return result
    def generate(left, right, solution):
        if right < left:
            return
        if not left and not right:
            result.append(solution)
        else:
            if left:
                generate(left-1, right, solution+'(')
            if right:
                generate(left, right-1, solution+')')
    generate(n, n, '')
    return result


if __name__ == '__main__':
    print generateParentheses(3)

