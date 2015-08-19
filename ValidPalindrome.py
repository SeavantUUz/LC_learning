# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/19'


def isPalindrome(s):
    if not s:
        return True
    length = len(s)
    left = 0
    right = length - 1
    while left <= right:
        a = s[left]
        b = s[right]
        if not a.isalnum():
            left += 1
        elif not b.isalnum():
            right -= 1
        else:
            a = a.lower()
            b = b.lower()
            if a != b:
                break
            else:
                left += 1
                right -= 1
    else:
        return True
    return False


if __name__ == '__main__':
    a = 'A man, a plan, a canal: Panama'
    print isPalindrome(a)

