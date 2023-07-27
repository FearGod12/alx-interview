#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """utf-8 validates a list of containing integers"""
    if not data:
        return True
    try:
        assert type(data) == list
    except AssertionError:
        return False
    count = 0
    for each in data:
        if type(each) is not int:
            return False
        binary = bin(each)[-2:]
        if each < 128:
            binary = '0' + binary
        if len(binary) > 8:
            binary = binary[-8:]
        if binary.startswith('0'):
            continue
        elif binary.startswith('10') and not binary[count + 1]:
            return False
        elif binary.startswith('110') and not binary[count + 2]:
            return False
        elif binary.startswith('1110') and not binary[count + 3]:
            return False
    return True
