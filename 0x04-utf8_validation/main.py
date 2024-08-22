#!/usr/bin/python3
"""
Main file for testing UTF-8 validation
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# Test case 1: Single valid ASCII character
data = [65]
print(f"Test Case 1 - Expected: True, Got: {validUTF8(data)}")

# Test case 2: Multiple valid ASCII characters
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(f"Test Case 2 - Expected: True, Got: {validUTF8(data)}")

# Test case 3: Valid 2-byte UTF-8 character (ñ)
data = [0b11000011, 0b10110001]  # 0xC3 0xB1
print(f"Test Case 3 - Expected: True, Got: {validUTF8(data)}")

# Test case 4: Valid 3-byte UTF-8 character (€)
data = [0b11100010, 0b10000010, 0b10000010]  # 0xE2 0x82 0x82
print(f"Test Case 4 - Expected: True, Got: {validUTF8(data)}")

# Test case 5: Valid 4-byte UTF-8 character (𐍈)
data = [0b11110000, 0b10011111, 0b10001101, 0b10001000]  # 0xF0 0x9F 0x94 0x88
print(f"Test Case 5 - Expected: True, Got: {validUTF8(data)}")

# Test case 6: Invalid UTF-8 sequence (overlong encoding)
data = [0b11000000, 0b10000000]  # Overlong encoding of a single ASCII character
print(f"Test Case 6 - Expected: False, Got: {validUTF8(data)}")

# Test case 7: Invalid 2-byte sequence (not enough bytes)
data = [0b11000011]  # Only one byte of a 2-byte sequence
print(f"Test Case 7 - Expected: False, Got: {validUTF8(data)}")

# Test case 8: Invalid 3-byte sequence (not enough bytes)
data = [0b11100010, 0b10000010]  # Only two bytes of a 3-byte sequence
print(f"Test Case 8 - Expected: False, Got: {validUTF8(data)}")

# Test case 9: Invalid byte values (out of range)
data = [256]  # 256 is out of the valid byte range (0-255)
print(f"Test Case 9 - Expected: False, Got: {validUTF8(data)}")

# Test case 10: Mixed valid and invalid bytes
data = [0b11000011, 0b10110001, 0b11100010, 0b10000010, 0b10000010, 0b11111111]
print(f"Test Case 10 - Expected: False, Got: {validUTF8(data)}")

# Test case 11: Empty data set
data = []
print(f"Test Case 11 - Expected: True, Got: {validUTF8(data)}")

# Test case 12: Valid multi-byte sequence followed by invalid byte
data = [0b11100010, 0b10000010, 0b10000010, 0b11111111]  # Last byte is invalid
print(f"Test Case 12 - Expected: False, Got: {validUTF8(data)}")

# Test case 13: Only single byte valid UTF-8 character (A) but mixed with invalid bytes
data = [65, 256]  # 256 is out of valid byte range
print(f"Test Case 13 - Expected: False, Got: {validUTF8(data)}")

# Test case 14: Correctly encoded but too short UTF-8 sequence (missing one byte for 4-byte character)
data = [0b11110000, 0b10011111, 0b10001101]  # Missing the last byte
print(f"Test Case 14 - Expected: False, Got: {validUTF8(data)}")
