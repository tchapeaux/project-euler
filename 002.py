fibo1 = 1
fibo2 = 2
newFibo = 0
currentSum = 0
fiboMax = 4000000
while (fibo2 < fiboMax):
    fibo1, fibo2 = fibo2, fibo1 + fibo2
    if (fibo2 % 2 == 0):
        currentSum += fibo2
    print(fibo1, fibo2, currentSum)
