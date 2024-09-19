#!/usr/bin/python3
""" making change problem """


def makeChange(coins, total, memo=None):
    """ determine the fewest number of coins needed to meet a
    given amount total """
    if total <= 0:
        return 0

    if memo is None:
        memo = {}
        coins.sort(reverse=True)
    minimum = -1
    for coin in coins:
        if total - coin >= 0:
            temp = memo.get(total - coin)
            if temp is not None:
                if temp != -1:
                    return temp + 1
            else:
                path = makeChange(coins, total - coin, memo)
                memo[total - coin] = path
                if path != -1:
                    return path + 1

    return -1
