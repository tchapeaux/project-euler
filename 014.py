def collatz_next(n):
    assert n == int(n)
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


KNOWN_LENGTHS = {1: 1}


def collatz_length(n):
    assert 1 in KNOWN_LENGTHS
    if n == 1:
        return 1
    values = [n]
    while n != 1:
        n_next = collatz_next(values[-1])
        if n_next in KNOWN_LENGTHS:
            for i, val in enumerate(reversed(values)):
                KNOWN_LENGTHS[val] = KNOWN_LENGTHS[n_next] + i + 1
            return KNOWN_LENGTHS[values[0]]
        else:
            values.append(n_next)

assert collatz_length(2) == 2
assert collatz_length(5) == 6
assert collatz_length(13) == 10, collatz_length(13)


current_max_length = 0
current_max_i = None
N = 1000000
for i in range(1, N + 1):
    if i % 10000 == 0:
        print(i, current_max_length)
    length = collatz_length(i)
    if length >= current_max_length:
        current_max_i = i
        current_max_length = length

print(current_max_i, "produces length", current_max_length)
# collatz_length(current_max_i)
