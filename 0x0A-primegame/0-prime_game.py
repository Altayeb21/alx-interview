#!/usr/bin/python3
""" prime game module """


def isWinner(x, nums):
    """ determine the player winned the most rounds """
    if type(x) != int:
        return None
    if type(nums) != list:
        return None
    if x <= 0:
        return None
    Ben = 0
    Maria = 0
    round_winner = 2
    for i in range(x):
        round_winner = 2
        num = nums[i]
        number_list = [j for j in range(2, num + 1)]
        while len(number_list) > 0:
            round_winner = 1 if round_winner == 2 else 2
            prime = number_list[0]
            to_remove = prime
            multiplier = prime
            while to_remove <= num:
                try:
                    number_list.remove(to_remove)
                    to_remove = prime * multiplier
                    multiplier += 1
                except ValueError:
                    to_remove = prime * multiplier
                    multiplier += 1
        if round_winner == 2:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    else:
        return None
