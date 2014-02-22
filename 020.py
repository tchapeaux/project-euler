import math

bigNum = math.factorial(100)
digitSum = 0
for char in str(bigNum):
    digitSum += int(char)
print(digitSum)
