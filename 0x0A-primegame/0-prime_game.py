#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_multiples(n, nums):
    """Remove multiples of n from the list of numbers"""
    return [num for num in nums if num % n != 0]

def play_round(n):
    """Play a round of the game"""
    nums = list(range(1, n + 1))
    winner = None
    while True:
        if not any(is_prime(num) for num in nums):
            break
        if winner is None:
            for num in nums:
                if is_prime(num):
                    nums = remove_multiples(num, nums)
                    winner = "Maria"
                    break
        else:
            for num in nums:
                if is_prime(num):
                    nums = remove_multiples(num, nums)
                    winner = "Ben"
                    break
    return winner

def isWinner(x, nums):
    """Determine the winner of the game"""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
