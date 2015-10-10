# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/10'


def majorityElement(nums):
    result = []
    # a, b, ca, cb = 0, 0, 0, 0
    # 这里a,b之所以不能取0,0是因为[0,0,0]这种情况……
    a, b, ca, cb = 0, 1, 0, 0
    for num in nums:
        if a == num:
            ca += 1
        elif b == num:
            cb += 1
        elif ca == 0:
            a, ca = num, 1
        elif cb == 0:
            print b
            b, cb = num, 1
            print b
        else:
            ca -= 1
            cb -= 1
    ta = len([1 for num in nums if num == a])
    tb = len([1 for num in nums if num == b])
    length = len(nums)
    print a, b
    if ta > length / 3:
        result.append(a)
    if tb > length / 3:
        result.append(b)
    return result

if __name__ == '__main__':
    print majorityElement([1,2])