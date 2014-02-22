# Lattice paths are modeled as bit-words (0: horizontal, 1: vertical)
# So the problem becomes:
# Find the number of different words of size 2n with exactly n 0's and n 1's
# i.e. the central binomial coefficient (2N choose N)

import math
fac = math.factorial


def n_choose_k(n, k):
    assert n == int(n)
    assert k == int(k)
    return int(fac(n) / (fac(k) * fac(n-k)))

N = 20

print(n_choose_k(2 * N, N))
