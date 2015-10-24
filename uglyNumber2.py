# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/23'


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = 0
        k = 0
        numbers = [1] * n
        for index in xrange(1, n):
            value = min([numbers[i] * 2, numbers[j] * 3, numbers[k] * 5])
            numbers[index] = value
            if value == numbers[i] * 2:
                i += 1
            if value == numbers[j] * 3:
                j += 1
            if value == numbers[k] * 5:
                k += 1
        return numbers[n-1]


if __name__ == '__main__':
    s = Solution()
    print s.nthUglyNumber(10)

