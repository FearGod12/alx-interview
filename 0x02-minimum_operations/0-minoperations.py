#!/usr/bin/python3
"""Minimum operations using the prime_factors method"""


def minOperations(n):
    factors = []

    # Divide by 2 repeatedly until it is no longer divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Divide by odd numbers starting from 3 up to the square root of n
    # Since any remaining factor must be prime
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 2, it is a prime factor itself
    if n > 2:
        factors.append(n)

    return sum(factors)
