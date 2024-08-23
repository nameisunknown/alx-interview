#!/usr/bin/python3
"""
This module validates if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masking to check the significant bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determining the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask = mask >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Checking that the next byte starts with '10'
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
