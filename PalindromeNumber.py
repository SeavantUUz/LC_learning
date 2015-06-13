# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/13'

def PalindromeNumber(x):
    ori_x = x
    if x < 0:
        # sign = -1
        # x = abs(x)
        return False
    palindrome_result = 0
    while x:
        r = x % 10
        palindrome_result = palindrome_result * 10 + r
        x /= 10
    # palindrome_result *= sign
    if palindrome_result == ori_x:
        return True
    else:
        return False


if __name__ == '__main__':
    print PalindromeNumber(1)
    print PalindromeNumber(121)
    print PalindromeNumber(123)
    print PalindromeNumber(-121)
