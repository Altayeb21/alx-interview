#!/usr/bin/python3
""" making change problem """


from typing import List, Mapping


def makeChange(coins: List, total: int, memo: Mapping=None):
    """ determine the fewest number of coins needed to meet a
    given amount total
    if total <= 0:
        return 0
    if len(coins) <= 0:
        return -1

    if memo is None:
        memo = {}
        coins.sort(reverse=True)
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
    return -1"""
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
