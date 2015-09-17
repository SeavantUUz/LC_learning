# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/17'


def isHappy(n):
    dup_dict = {1:1}
    def helper(n):
        result = 0
        while n:
            p = n % 10
            result += p*p
            n /= 10
        return result
    while n not in dup_dict:
        dup_dict[n] = 1
        n = helper(n)
    if n == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print isHappy(19)