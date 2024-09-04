#!/usr/bin/python3
# 0-prime_game.py

def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Generate a sieve to find prime numbers up to the max number in nums
    def generate_primes(n):
        primes = []
        sieve = [True] * (n + 1)
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for multiple in range(p * p, n + 1, p):
                    sieve[multiple] = False
        return primes

    # Game simulation function
    def play_game(n):
        primes = generate_primes(n)
        taken = [False] * (n + 1)
        moves = 0
        for prime in primes:
            if not taken[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    taken[multiple] = True
        return moves % 2 == 1  # If odd moves, Maria wins, else Ben wins

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
