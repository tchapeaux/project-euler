import math


factorials = {str(i): math.factorial(i) for i in range(10)}

llist = []
upperBound = 10000000  # 7 * 9! < 9999999
for i in range(3, upperBound):
    string = str(i)
    summ = 0
    for char in string:
        summ += factorials[char]
    if summ == i:
        llist.append(i)

print(llist)
print(sum(llist))
