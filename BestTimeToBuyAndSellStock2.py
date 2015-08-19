# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/19'


def maxProfit(prices):
    profit = 0
    length = len(prices)
    if not length:
        return 0
    for i in xrange(1, length):
        profit += max(0, prices[i] - prices[i-1])
    return profit


if __name__ == '__main__':
    a = [1,7, 5,4, 11]
    print maxProfit(a)