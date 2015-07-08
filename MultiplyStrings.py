# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/6'

def multiply(num1, num2):
    size1 = len(num1)
    size2 = len(num2)
    result = [0] * (size1 + size2)
    j = size2 - 1
    while j >= 0:
        a = int(num2[j])
        i = size1 - 1
        while i >= 0:
            b = int(num1[i])
            k = i + j + 1
            result[k] += a * b
            i-=1
        j-=1
    size = len(result)
    ad = 0
    while size > 0:
        k = size - 1
        num = result[k] + ad
        p = num % 10
        result[k] = p
        ad = num / 10
        size -= 1
    m = 0
    for index, e in enumerate(result):
        if e != 0:
            m = index
            break
    else:
        return '0'
    answer = ''.join([str(i) for i in result[m:]])
    return answer

if __name__ == '__main__':
    print multiply('2', '1')
