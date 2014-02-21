N = 100
l = range(1, N + 1)

currentSum = 0
for i in range(N):
    for j in range(i + 1, N):
        currentSum += 2 * l[i] * l[j]

print(currentSum)
