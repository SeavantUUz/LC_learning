# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/26'

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrts = []
        i = 1
        while i * i <= n:
            sqrts.append(i * i)
            i += 1
        r = set([n])
        level = 0
        while r:
            temp = set()
            level += 1
            for val in r:
                for i in sqrts:
                    if i > val:
                        continue
                    delta = val - i
                    if delta == 0:
                        return level
                    temp.add(delta)
            r = temp
        return level


if __name__ == '__main__':
    s = Solution()
    print s.numSquares(12)


