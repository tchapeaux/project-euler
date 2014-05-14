import math

with open("500000_PRIMES.txt") as f:
    PRIMES = [int(p) for p in f.read().split()]


def primesBelow(n):
    assert n > 0
    if n < PRIMES[-1]:
        n_index = 0
        while PRIMES[n_index] < n:
            n_index += 1
        return PRIMES[:n_index]
    else:
        primes = PRIMES
        for i in range(primes[-1] + 2, n + 1, 2):
            is_prime = True
            for p in primes:
                if p > math.sqrt(i):
                    break
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes
