#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 71
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 121
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = -1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = "hello"
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3.2
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 91
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
