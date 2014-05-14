fifthpowers = {str(i): i ** 5 for i in range(10)}

llist = []
upperBound = 1000000  # 6 * 9^5 < 999999
for i in range(3, upperBound):
    string = str(i)
    summ = 0
    for char in string:
        summ += fifthpowers[char]
    if summ == i:
        llist.append(i)

print(llist)
print(sum(llist))
