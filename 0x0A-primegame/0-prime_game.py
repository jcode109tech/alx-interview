#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Use Sieve of Eratosthenes to find all primes up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for start in range(2, int(n**0.5) + 1):
        if primes[start]:
            for multiple in range(start * start, n + 1, start):
                primes[multiple] = False
    return primes

def count_prime_moves(n, primes):
    """Count how many prime numbers can be picked optimally."""
    multiples_removed = [False] * (n + 1)
    prime_count = 0
    
    for num in range(2, n + 1):
        if primes[num] and not multiples_removed[num]:
            # If `num` is prime and still in the set, it's Maria's turn.
            prime_count += 1
            # Remove `num` and all its multiples from the set.
            for multiple in range(num, n + 1, num):
                multiples_removed[multiple] = True
    
    return prime_count

def isWinner(x, nums):
    """Determine who wins the most games."""
    if x < 1 or not nums:
        return None
    
    # Precompute primes up to the maximum number in `nums` using Sieve of Eratosthenes
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    # Play the game for each `n` in `nums`
    for n in nums:
        prime_moves = count_prime_moves(n, primes)
        # If the number of moves (prime picks) is odd, Maria wins because she starts first.
        # If it's even, Ben wins because Maria's turn will be the last.
        if prime_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
