# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/18'

def letterCombineOfPhoneNumber(digits):
    size = len(digits)
    mapping = {'0':' ', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
    result = []
    if not digits:
        return result
    def dfs(index, solution):
        if index == size - 1:
            char = digits[index]
            alphas = mapping[char]
            for alpha in alphas:
                result.append(solution + alpha)
            return
        char = digits[index]
        alphas = mapping[char]
        for alpha in alphas:
            dfs(index+1, solution+alpha)
    dfs(0, '')
    return result


if __name__ == '__main__':
    print letterCombineOfPhoneNumber('')
