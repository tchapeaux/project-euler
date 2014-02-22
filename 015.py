# Lattice paths are modeled as bit-words (0: horizontal, 1: vertical)
# So the problem becomes:
# Find the number of different words of size 2n with exactly n 0's and n 1's
# This script tries to count them stupidly and takes forever

import itertools

# N = 20 # Bad idea
N = 10

counter = 0

for word in itertools.product([0, 1], repeat=2 * N):
    count0 = word.count(0)
    count1 = word.count(1)
    if count0 == count1:
        # print(word)
        counter += 1

print(counter)
