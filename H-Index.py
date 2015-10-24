# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/24'


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        cs = sorted(citations, reverse=True)
        prev = 0
        for index, num in enumerate(cs):
            current = index + 1
            if current == num:
                return current
            elif current > num:
                return prev
            else:
                prev = current
        return prev


if __name__ == '__main__':
    s = Solution()
    print s.hIndex([1])
