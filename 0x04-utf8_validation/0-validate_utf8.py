#!/usr/bin/python3
""" utf-8 validation """


def validUTF8(data):
    """ validate if a data is utf-8 encoded """
    count = 0
    for byte in data:
        binary = bin(byte & 255)[2:]
        if len(binary) < 8:
            if count:
                return False
            continue
        if not count:
            for i in range(4):
                if binary[i] == '1':
                    count += 1
            count -= 1
            if count > 3:
                return False
            if binary[count + 1:] == "0" * (8 - (count + 1)):
                return False
        else:
            if binary[:2] == "10":
                count -= 1
                continue
            return False
    if count:
        return False
    return True
