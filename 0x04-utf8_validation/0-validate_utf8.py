#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """
    UTF-8 validation function that checks if the input list of integers
    represents a valid UTF-8 sequence.

    :param data: A list of integers representing bytes in a UTF-8 sequence.
    :return: True if the input is a valid UTF-8 sequence, False otherwise.
    """

    if len(data) == 0:
        # If the input list is empty, it is considered a valid UTF-8 sequence.
        return True

    try:
        assert type(data) == list
        # Ensure that the input data is a list.
    except AssertionError:
        # If the input is not a list, it is not a valid UTF-8 sequence.
        return False

    index = 0
    count = 0
    for each in data:
        # Loop through each element in the input list.

        index += 1

        if (type(each) != int) or each > 255 or each < 0:
            # Check if each element is a valid 8-bit unsigned integer
            # (0 to 255).
            # If not, it is not a valid UTF-8 sequence.
            return False

        binary_data = format(each, '08b')
        # Get the binary representation of the current byte.

        if each < 128:
            # Single-byte UTF-8 character (0xxxxxxx).
            count = 0
        elif binary_data.startswith('110'):
            # Two-byte UTF-8 character (110xxxxx 10xxxxxx).
            count = 1
        elif binary_data.startswith('1110'):
            # Three-byte UTF-8 character (1110xxxx 10xxxxxx 10xxxxxx).
            count = 2
        elif binary_data.startswith('11110'):
            # Four-byte UTF-8 character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx).
            count = 3

        j = index
        for _ in range(count):
            # Loop to check continuation bytes for multi-byte characters.

            if data[j + 1]:
                # Check if there is a continuation byte available.
                binary = format(data[j + 1], '08b')
                if not binary.startswith('10'):
                    # If the continuation byte doesn't start with '10',
                    # it is not a valid UTF-8 sequence.
                    return False
            else:
                # If there is no continuation byte available,
                # it is not a valid UTF-8 sequence.
                return False

        count = 0

    return True
