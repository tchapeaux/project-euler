from functools import reduce

list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19]

x = reduce(lambda x, y: x * y, list_of_primes)
remainder = -1
while remainder != 0:
    for j in range(20):
        remainder = x % (j + 1)
        if remainder != 0:
            print(x, "not divisible by", (j + 1))
            break
    if remainder != 0:
        for p in list_of_primes:
            if remainder % p == 0:
                x = x * p
                break
print(x, "is divisible by 1..20")
