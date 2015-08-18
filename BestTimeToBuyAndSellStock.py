# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/18'


def maxProfit(prices):
    length = len(prices)
    if not length:
        return 0
    profit_cur = 0
    profit_so_far = 0
    for i in xrange(1, length):
        profit_cur = max(0, profit_cur+prices[i]-prices[i-1])
        profit_so_far = max(profit_cur, profit_so_far)
    return profit_so_far


if __name__ == '__main__':
    a = [1,7, 4, 11]
    print maxProfit(a)
