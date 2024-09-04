#!/usr/bin/python3
"""
Prime Game Module
"""

def sieve_of_eratosthenes(n):
    """
    Generate prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    
    :param x: number of rounds
    :param nums: array of n for each round
    :return: name of the player that won the most rounds, or None if it's a tie
    """
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = sum(primes[:n+1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
