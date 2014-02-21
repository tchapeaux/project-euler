currentsum = 0
mul3 = 0
while (mul3 < 1000):
    currentsum += mul3
    mul3 += 3
mul5 = 0
while (mul5 < 1000):
    currentsum += mul5
    mul5 += 5
    if (mul5 % 3 == 0):
        mul5 += 5

print(currentsum)
