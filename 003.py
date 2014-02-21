# number for problem 3 : 600851475143
x = 600851475143
d = 1
while (d < x):
    d += 1
    if (x % d == 0):
        print(d, "divides", x)
        x = x / d
        d -= 1
