import math
foundA, foundB, foundC = 0, 0, 0
for a in range(1, 1000):
    if (foundA != 0):
        break
    for b in range(a, 1000):
        c = math.sqrt(a * a + b * b)  # may not be an integer
        if a + b + c == 1000:
            c = int(c)  # better formatting
            print(a, b, c, "because", a * a, "+", b * b, "=", c * c)
            foundA, foundB, foundC = a, b, int(c)
            break
print(foundA*foundB*foundC)
