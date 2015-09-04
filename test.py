# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/4'


def test(l1, l2):
    l1.extend(l2)
    l1.sort(key=lambda item:item[0])
    result = []
    min_point, max_point = l1[0]
    for low, high in l1[1:]:
        if low > max_point:
            result.append((min_point, max_point))
        if low > min_point:
            min_point = low
        if high < max_point:
            max_point = high
    return result

if __name__ == '__main__':
    print test([(1,4), (2,3), [1,5], [4,6]], [(2,5), (6, 7)])