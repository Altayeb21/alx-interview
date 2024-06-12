#!/usr/bin/python3
""" minimum operations """


def minOperations(n):
    """ find the minimum number of operations needed to result
    in n 'H' characters in a file only using CopyAll and Paste
    operations """
    if type(n) != int or n < 2:
        return 0
    prime_factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n /= divisor
            prime_factors.append(divisor)
            continue
        divisor += 1

    return sum(prime_factors)
