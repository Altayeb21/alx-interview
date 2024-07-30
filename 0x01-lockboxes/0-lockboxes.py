#!/usr/bin/python3
""" lockeboxes problem """


def canUnlockAll(boxes):
    """ determines if all boxes can opened """
    if type(boxes) != list:
        return False
    if len(boxes) <= 1:
        return True
    length = len(boxes)
    used_keys = set([0])
    new_keys = set()
    opend = 0
    to_use_keys = set([0])
    while len(to_use_keys) != 0:
        for key in to_use_keys:
            if key < length and key >= 0:
                if type(boxes[key]) != list:
                    return False
                new_keys = new_keys | set(boxes[key])
                opend += 1
                # print(f"opend box number: {key}, opend: {opend}")
        if (opend == length):
            return True
        to_use_keys = new_keys - used_keys
        used_keys |= new_keys
        new_keys = set()
    return False
