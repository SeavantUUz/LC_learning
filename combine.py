# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/24'


def combine(n, k):
    result = []
    def one_solution(solution, num, k):
        if num > n + 1 or k < 0:
            return
        elif k == 0:
            result.append(solution[:])
            return
        else:
            one_solution(solution, num+1, k)
            solution.append(num)
            one_solution(solution, num+1, k-1)
            solution.pop()
    one_solution([], 1, k)
    return result


if __name__ == '__main__':
    print combine(4,2)
