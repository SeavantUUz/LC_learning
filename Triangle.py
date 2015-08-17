# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/17'


def minimumTotal0(triangle):
    depth = len(triangle)
    def sub_minimum(left, right, level):
        if level == depth:
            return 0
        return min(triangle[level][left] + sub_minimum(left, left+1, level+1),
                   triangle[level][right] + sub_minimum(right, right+1, level+1) )
    if depth == 1:
        return triangle[0][0]
    return triangle[0][0] + sub_minimum(0, 1, 1)


def minimumTotal(triangle):
    f = [0] * (len(triangle) + 1)
    for row in triangle[::-1]:
        for i in xrange(len(row)):
            f[i] = row[i] + min(f[i], f[i+1])
    return f[0]



if __name__ == '__main__':
    a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print minimumTotal(a)