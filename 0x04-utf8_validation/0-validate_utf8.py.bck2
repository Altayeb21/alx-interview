#!/usr/bin/python3
""" utf-8 validation """


def validUTF8(data):
    """Validate if a data set is a valid UTF-8 encoding."""
    count = 0
    for byte in data:
        # Get the binary representation of the byte
        binary = bin(byte)[2:].rjust(8, '0')

        if count == 0:
            # Determine the number of leading 1s in the byte
            if binary.startswith('0'):
                # Single-byte character (ASCII)
                continue
            elif binary.startswith('110'):
                # 2-byte character
                count = 1
            elif binary.startswith('1110'):
                # 3-byte character
                count = 2
            elif binary.startswith('11110'):
                # 4-byte character
                count = 3
            else:
                # Invalid starting byte
                return False
        else:
            # Check continuation byte
            if binary.startswith('10'):
                count -= 1
            else:
                # Invalid continuation byte
                return False

    # Check if all multi-byte sequences are properly closed
    return count == 0
