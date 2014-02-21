import math
N = 2000000

list_of_primes = [2]
x = 1
theSum = 2
while x < N - 1:
    x += 2
    divisor_found = False
    for p in list_of_primes:
        if x % p == 0:
            divisor_found = True
            break
    if not divisor_found:
        print(x)
        theSum += x
        if x < math.sqrt(N):
            list_of_primes.append(x)
print(theSum)
