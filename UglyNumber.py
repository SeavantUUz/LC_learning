# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/21'


# class Solution(object):
#     def isUgly(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num == 1:
#             return True
#         else:
#             if num % 5 == 0:
#                 return self.isUgly(num / 5)
#             elif num % 3 == 0:
#                 return self.isUgly(num / 3)
#             elif num % 2 == 0:
#                 return self.isUgly(num / 2)
#             else:
#                 return False


class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        while num != 1:
            if not num % 5:
                num /= 5
            elif not num % 3:
                num /= 3
            elif not num % 2:
                num /= 2
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print s.isUgly(0)
    print s.isUgly(3)
    print s.isUgly(6)
    print s.isUgly(8)
    print s.isUgly(14)
    print s.isUgly(30)
