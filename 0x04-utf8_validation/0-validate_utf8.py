#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """
    UTF-8 validation function that checks if the input list of integers
    represents a valid UTF-8 sequence.

    :param data: A list of integers representing bytes in a UTF-8 sequence.
    :return: True if the input is a valid UTF-8 sequence, False otherwise.
    """

    def is_continuation_byte(byte):
        # Helper function to check if the byte is a continuation byte
        # (starts with '10').
        return 128 <= byte <= 191

    if len(data) == 0:
        # If the input list is empty, it is considered a valid UTF-8 sequence.
        return True

    if not isinstance(data, list):
        # Ensure that the input data is a list.
        return False

    count = 0
    for each in data:
        # Loop through each element in the input list.

        if not isinstance(each, int):
            # Check if each element is a valid 8-bit unsigned integer
            # (0 to 255).
            # If not, it is not a valid UTF-8 sequence.
            return False

        # Consider only the last 8 bits of the integer.
        each = each % 256

        if each < 128:
            # Single-byte UTF-8 character (0xxxxxxx).
            count = 0
        elif each >> 5 == 0b110:
            # Two-byte UTF-8 character (110xxxxx 10xxxxxx).
            count = 1
        elif each >> 4 == 0b1110:
            # Three-byte UTF-8 character (1110xxxx 10xxxxxx 10xxxxxx).
            count = 2
        elif each >> 3 == 0b11110:
            # Four-byte UTF-8 character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx).
            count = 3
        else:
            # Invalid UTF-8 encoding pattern.
            return False

        for j in range(count):
            # Loop to check continuation bytes for multi-byte characters.
            if len(data) > j + 1:
                next_byte = data[j + 1]

                if not is_continuation_byte(next_byte):
                    # If the continuation byte doesn't start with '10',
                    # it is not a valid UTF-8 sequence.
                    return False
            else:
                # If there is no continuation byte available,
                # it is not a valid UTF-8 sequence.
                return False

    return True
