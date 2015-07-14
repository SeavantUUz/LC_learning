# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/14'


def spiralMatrix2(n):
    dup_dict = dict()
    vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def change_direction(direction):
        if direction == 3:
            return 0
        else:
            return direction + 1

    def generate_next(x, y, direction):
        next_x = x + vector[direction][0]
        next_y = y + vector[direction][1]
        if next_x == n or next_y == n or next_x < 0 or next_y < 0:
            direction = change_direction(direction)
            next_x = x + vector[direction][0]
            next_y = y + vector[direction][1]
        hit = dup_dict.get((next_x, next_y))
        if hit:
            direction = change_direction(direction)
            next_x = x + vector[direction][0]
            next_y = y + vector[direction][1]
            hit_again = dup_dict.get((next_x, next_y))
            if hit_again:
                return 0, 0, direction
        dup_dict[(next_x, next_y)] = 1
        return next_x, next_y, direction

    if n == 0:
        return []
    if n == 1:
        return [[1]]
    x = y = direction = 0
    index = 1
    result = []
    for i in xrange(n):
        result.append([])
        for j in xrange(n):
            result[i].append(0)
    result[0][0] = 1
    dup_dict[(0, 0)] = index
    while True:
        index += 1
        x, y, direction = generate_next(x, y, direction)
        if x == 0 and y == 0:
            return result
        else:
            result[x][y] = index


if __name__ == '__main__':
    print spiralMatrix2(21)
