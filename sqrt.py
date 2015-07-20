# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/20'


def mySqrt(x):
    left = 0
    right = x
    mid = 0
    while left <= right:
        mid = (left + right) / 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            if (mid+1) * (mid+1) == x:
                return mid + 1
            elif (mid+1) * (mid+1) < x:
                left = mid + 1
            else:
                return mid
        else:
            print mid
            if (mid-1) * (mid-1) == x:
                return mid - 1
            elif (mid-1) * (mid-1) < x:
                return mid - 1
            else:
                right = mid - 1
    return mid


if __name__ == '__main__':
    print mySqrt(6)