#!/usr/bin/python3
# 0-prime_game.py

def isWinner(x, nums):
    """
    Determines the winner of each round of the Prime Game.
    
    Args:
    x: Number of rounds.
    nums: List of integers representing the upper bound for each round.
    
    Returns:
    The name of the player who won the most rounds (Maria or Ben).
    If there's a tie or no winner can be determined, returns None.
    """
    
    def generate_primes(n):
        """
        Generates a list of prime numbers up to n using Sieve of Eratosthenes.
        """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        return primes

    def play_game(n):
        """
        Simulates one round of the game.
        Maria plays first, and players alternate turns, removing primes and their multiples.
        Returns True if Maria wins, False if Ben wins.
        """
        primes = generate_primes(n)
        taken = [False] * (n + 1)
        moves = 0
        for prime in primes:
            if not taken[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    taken[multiple] = True
        return moves % 2 == 1  # Maria wins if odd number of moves, else Ben wins

    # Track wins for both Maria and Ben
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


# Test Framework
def test_prime_game():
    """
    Tests the isWinner function with multiple test cases and logs the results.
    """
    tests = [
        # (x, nums, expected_result)
        (5, [2, 5, 1, 4, 3], "Ben"),
        (3, [4, 5, 1], "Ben"),
        (1, [1], "Ben"),
        (2, [1, 2], "Maria")
    ]
    
    for test_num, (x, nums, expected) in enumerate(tests, start=1):
        try:
            print(f"Test {test_num}: Running with x={x}, nums={nums}")
            result = isWinner(x, nums)
            
            # Check text answer correctness
            if result == expected:
                print(f"Test {test_num}: Text answer success (Expected: {expected}, Got: {result})")
            else:
                print(f"Test {test_num}: Text answer fail (Expected: {expected}, Got: {result})")
            
        except Exception as e:
            print(f"Test {test_num}: Code fail with error: {e}")
        
        # Additional checks like performance/efficiency could be done separately

if __name__ == "__main__":
    # Run the test cases to validate the implementation
    test_prime_game()
