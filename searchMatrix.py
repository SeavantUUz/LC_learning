# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/23'

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = n-1
    mid = 0
    while left <= right:
        mid = (left + right) / 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            right = mid - 1
        else:
            left = mid + 1
    if mid > 0:
        if matrix[mid-1][0] < target < matrix[mid][0]:
            mid = mid - 1
    row = mid
    left = 0
    right = m-1
    while left <= right:
        mid = (left + right) / 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == '__main__':
    print searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11)

