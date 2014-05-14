from primes import primesBelow


def rotations(word):
    for shift in range(len(word)):
        yield word[shift:] + word[:shift]

count = 0
primes = set(primesBelow(1000000))
for i, prime in enumerate(primes):
    allRotArePrimes = True
    for rot in rotations(str(prime)):
        if int(rot) not in primes:
            allRotArePrimes = False
            break
    if allRotArePrimes:
        count += 1

print("count is", count)
