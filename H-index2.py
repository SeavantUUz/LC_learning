# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/24'


# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         if not citations:
#             return 0
#         else:
#             length = len(citations)
#             index = length - 1
#             current = 1
#             prev = 0
#             while index >= 0:
#                 if current == citations[index]:
#                     return current
#                 elif current > citations[index]:
#                     return prev
#                 else:
#                     prev = current
#                     current += 1
#                     index -= 1
#             return prev


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        else:
            length = len(citations)
            left = 0
            right = length
            while left < right:
                # fuck
                mid = ((right - left) >> 1) + left
                pos = length - mid
                if citations[mid] == pos:
                    return pos
                elif citations[mid] < pos:
                    left = mid + 1
                else:
                    right = mid
            return length - left

if __name__ == '__main__':
    s = Solution()
    print s.hIndex([0,0,0])
