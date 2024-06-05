#!/usr/bin/python3
""" locked boxes problem solution """


def canUnlockAll(boxes):
    if type(boxes) != list:
        return False
    keys = set()
    opend = []
    flag = False
    keys |= set(boxes[0])
    opend.append(0)
    newkeys = set()
    while (len(opend) < len(boxes)):
        newkeys = set()
        if len(keys) == 0:
            break
        for i in keys:
            if (i < len(boxes)):
                if (i not in opend):
                    opend.append(i)
                    newkeys |= set(boxes[i])
                    if len(opend) == len(boxes):
                        flag = True
                        break
        keys = newkeys - keys
    return flag
