#!/usr/bin/python3
"""Minimum operations"""


def isprime(n):
    """check if its a prime number"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def minOperations(n):
    """minimum operations"""
    if not isinstance(n, int) or n <= 1:
        return 0
    file = 'H'
    count = 0
    copyall = 'H'
    for i in range(1, n):
        if n % i == 0 and isprime(i):
            if len(file + copyall) <= n:
                count += 1
                copyall = file[:]
                count += 1
                file += copyall
        else:
            if len(file + copyall) <= n:
                file += copyall
                count += 1
    return count
