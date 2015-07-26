# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/26'


# direction in [1,2,3,4]
# 1 -> up
# 2 -> down
# 3 -> left
# 4 -> right
def wordSearch(board, word):
    m = len(board[0])
    n = len(board)
    slen = len(word)
    def pattern(word, finished, x, y, record):
        if not word[finished] == board[y][x]:
            return False
        if record.get((x, y)):
            return False
        if finished == slen - 1:
            return True
        is_success = False
        record[(x, y)] = True
        if not is_success and x > 0:
            is_success = pattern(word, finished+1, x-1, y, record)
        if not is_success and x < m-1:
            is_success = pattern(word, finished+1, x+1, y, record)
        if not is_success and y > 0:
            is_success = pattern(word, finished+1, x, y-1, record)
        if not is_success and y < n-1:
            is_success = pattern(word, finished+1, x, y+1, record)
        record[(x, y)] = False
        return is_success

    for y in xrange(n):
        for x in xrange(m):
            if pattern(word, 0, x, y, {}):
                return True
    return False


if __name__ == '__main__':
    print wordSearch(["ABCD", "SFCS", "ADEF"], 'ABCCED')
    print wordSearch(["a"], 'a')
    print wordSearch(["aa"], 'aaa')
    print wordSearch(['ab'], 'ba')
    print wordSearch(['aaaa', 'aaaa', 'aaaa'], 'aaaaaaaaaaaaa')
    print wordSearch(['CAA', 'AAA', 'BCD'], 'AAB')



