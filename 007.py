import math

list_of_primes = [2]
x = 1
while(len(list_of_primes) < 10001):
    x += 2
    upper_bound = math.ceil(math.sqrt(x))
    found_divisor = False
    for p in list_of_primes:
        if x % p == 0:
            found_divisor = True
            break
        if p > upper_bound:
            break
    if not found_divisor:
        list_of_primes.append(x)
        print("added", x)
print(x)
