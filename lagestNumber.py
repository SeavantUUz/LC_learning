# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/12'


def largestNumber(nums):
    max_length = len(str(max(nums)))
    result = []
    for num in nums:
        r = str(num)
        length = len(r)
        delta = max_length - length
        r1 = r+r[0] * delta
        r2 = r+ r[length-1] * delta
        r = max([r1, r2])
        result.append((int(r), str(num)))
    result.sort(key=lambda item: item[0], reverse=True)
    value = ''.join([item[1] for item in result])
    if value[0] == '0':
        return '0'
    else:
        return value


if __name__ == '__main__':
    # print largestNumber([3, 3088, 342, 5, 9, 98])
    print largestNumber([121, 12])
    print largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247])
