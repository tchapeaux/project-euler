import math

FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]


def primesBelow(n):
    assert n > 0
    if n < FIRST_PRIMES[-1]:
        n_index = 0
        while FIRST_PRIMES[n_index] < n:
            n_index += 1
        return FIRST_PRIMES[:n_index]
    else:
        primes = FIRST_PRIMES
        for i in range(primes[-1] + 1, n + 1):
            is_prime = True
            for p in primes:
                print(i, p)
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes


def smallestNumberDivisibleByAllBelow(n):
    assert n > 0
    primes = dict((p, 0) for p in primesBelow(n))
    print("primes below", n, ":", list(primes.keys()))
    # find minimal count for each primes to be a multiple of each number in 1..n
    for i in range(1, n + 1):
        for p in primes:
            count = 0
            while i % p == 0:
                count += 1
                i /= p
            if count > primes[p]:
                primes[p] = count
    # compute minimal number
    print("counts:", primes.items())
    num = 1
    for prime, count in primes.items():
        num *= int(math.pow(prime, count))
    return num

print(smallestNumberDivisibleByAllBelow(20))
