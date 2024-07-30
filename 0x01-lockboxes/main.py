#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes), "correct: True")

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes), "correct: True")

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes), "correct: False")

boxes = [[1, 10], [2, 5], [4], [3], [3], []]
print(canUnlockAll(boxes), "correct: True")

boxes = [[1, 10, 5], [2, 5, 1], [4, 2], [3, 7], [3], [], []]
print(canUnlockAll(boxes), "correct: False")

boxes = {}
print(canUnlockAll(boxes), "correct: False")

boxes = [[2], [], []]
print(canUnlockAll(boxes), "correct: False")

boxes = [[1]]
print(canUnlockAll(boxes), "correct: True")

boxes = [[]]
print(canUnlockAll(boxes), "correct: True")

