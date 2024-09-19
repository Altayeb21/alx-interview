#!/usr/bin/python3
""" making change problem """


def makeChange(coins, total, memo=None):
    """ determine the fewest number of coins needed to meet a
    given amount total """
    if total <= 0:
        return 0

    if memo is None:
        memo = {}
        coins.sort()
    minimum = -1
    for coin in coins:
        if total - coin >= 0:
            temp = memo.get(total - coin)
            if temp is not None:
                if temp != -1:
                    minimum = min(minimum, temp) if minimum != -1 else max(minimum, temp)
            else:
                path = makeChange(coins, total - coin, memo)
                memo[total - coin] = path
                if path != -1:
                    minimum = min(minimum, temp) if minimum != -1 else max(minimum, path)
        else:
            break

    return minimum + 1 if minimum != -1 else minimum
