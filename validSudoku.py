# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/4'


def validSudoku(board):
    line_size = len(board)
    column_dict = dict()
    row_dict = dict()
    area_dict = dict()
    for i in xrange(line_size):
        column_dict[i] = dict()
        row_dict[i] = dict()
        area_dict[i] = dict()
    for i, line in enumerate(board):
        for j, number in enumerate(line):
            area_index = i / 3 * 3 + j / 3
            if row_dict[i].get(number, 0) or column_dict[j].get(number, 0) or area_dict[area_index].get(number, 0):
                return False
            else:
                if number != '.':
                    row_dict[i][number] = 1
                    column_dict[j][number] = 1
                    area_dict[area_index][number] = 1
    return True
