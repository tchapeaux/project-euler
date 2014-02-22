bigNumString = str(2 ** 1000)
theSum = 0
for char in bigNumString:
    theSum += int(char)
print(theSum)
