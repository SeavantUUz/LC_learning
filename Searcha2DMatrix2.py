# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/17'

class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = matrix[0]
        y = self.binary_search(row, 0, len(row) - 1, target)
        column = [line[0] for line in matrix]
        x = self.binary_search(column, 0, len(column) - 1, target)
        row1 = matrix[x]
        row2 = [line[y] for line in matrix]
        a = self.binary_search(row1, 0, len(row1)-1, target)
        b = self.binary_search(row2, 0, len(row2)-1, target)
        return matrix[x][a] == target or matrix[b][y] == target


    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = ((right - left) >> 1) + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print
        return ((right-left) >> 1) + left

# 二分搜索会出现一些问题，下面的解法相当漂亮
# 思路是把x， y的增长（没法收缩）变成x，y一边增加一边减少
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix[0])
        m = len([row[0] for row in matrix])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        else:
            return False

if __name__ == '__main__':
    # m = [
  # [1,   4,  7, 11, 15],
  # [2,   5,  8, 12, 19],
  # [3,   6,  9, 16, 22],
  # [10, 13, 14, 17, 24],
  # [18, 21, 23, 26, 30]
# ]
    m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    s = Solution()
    print s.searchMatrix(m, 33)
