# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/5'


def restoreIpAddress(s):
    result = []
    length = len(s)
    duplicate_dict = dict()
    def get_one_solution(one_solution, start, step):
        if start >= length:
            return
        if len(one_solution) == 3:
            s_remain = s[start:]
            remain = int(s_remain)
            if remain > 255:
                return
            elif len(s_remain) != 1 and s_remain[0] == '0':
                return
            else:
                solution = one_solution[:]
                solution.append(s[start:])
                t = tuple(solution)
                if t not in duplicate_dict:
                    duplicate_dict[t] = 1
                    result.append('.'.join(solution))
                return
        if start + step >= length:
            return
        s_value = s[start:start+step]
        value = int(s_value)
        if value > 255:
            return
        elif len(s_value) != 1 and s_value[0] == '0':
            return
        else:
            one_solution.append(s_value)
            get_one_solution(one_solution[:], start+step, 1)
            get_one_solution(one_solution[:], start+step, 2)
            get_one_solution(one_solution[:], start+step, 3)
    get_one_solution([], 0, 1)
    get_one_solution([], 0, 2)
    get_one_solution([], 0, 3)
    return result


if __name__ == '__main__':
    print restoreIpAddress("010010")
