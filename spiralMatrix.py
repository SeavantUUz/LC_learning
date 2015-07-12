# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/12'


def spiralMatrix(matrix):
    result = []
    dup_dict = dict()
    if not matrix:
        return matrix
    m = len(matrix) - 1
    n = len(matrix[0]) - 1
    if m == 0 and n == 0:
        result.append(matrix[0][0])
        return result
    if m == 0:
        result = matrix[0]
        return result
    if n == 0:
        result = [item[0] for item in matrix]
        return result
    add_pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def get_next_position(current_pos, status):
        add_way = add_pos[status]
        next_pos = (current_pos[0] + add_way[0], current_pos[1] + add_way[1])
        if next_pos[0] > m or next_pos[1] > n or next_pos[0] < 0 or next_pos[1] < 0:
            status = change_status(status)
            add_way = add_pos[status]
            next_pos = (current_pos[0] + add_way[0], current_pos[1] + add_way[1])
        if dup_dict.get(next_pos):
            status = change_status(status)
            add_way = add_pos[status]
            next_pos = (current_pos[0] + add_way[0], current_pos[1] + add_way[1])
            if dup_dict.get(next_pos):
                return (), status
            else:
                dup_dict[next_pos] = 1
                return next_pos, status
        dup_dict[next_pos] = 1
        return next_pos, status

    def change_status(status):
        if status == 3:
            return 0
        else:
            return status + 1
    pos = (0, 0)
    result.append(matrix[pos[0]][pos[1]])
    dup_dict[(0, 0)] = 1
    status=0
    next_pos, status = get_next_position(pos, status)
    while next_pos:
        pos = next_pos
        result.append(matrix[pos[0]][pos[1]])
        next_pos, status = get_next_position(pos, status)
    return result


if __name__ == '__main__':
    matrix = [
        [1, 2]
    ]
    print spiralMatrix(matrix)

