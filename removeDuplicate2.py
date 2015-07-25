# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/25'


def removeDuplicate2(nums):
    if not nums:
        return 0
    index = 0
    toleration = 1
    pre = float('inf')
    for num in nums:
        if not num == pre:
            toleration = 1
        else:
            if not toleration:
                continue
            else:
                toleration -= 1
        pre = num
        nums[index] = num
        index += 1
    del nums[index:]
    return index

if __name__ == '__main__':
    print removeDuplicate2([1,1,1,2,2,3])


