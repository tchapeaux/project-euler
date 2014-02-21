import math


def is_palindrom(word):
    l = len(word)
    for i in range(math.floor(l / 2)):
        if word[i] != word[l-1-i]:
            return False
    return True

assert(is_palindrom("cacaacac"))
assert(is_palindrom("9229"))
assert(is_palindrom("KAYAKKAYAKKAYAKKAYAK"))
assert(is_palindrom("12321"))

assert(not is_palindrom("12345"))
assert(not is_palindrom("AZERTYXTREZA"))
assert(not is_palindrom("1234221"))

n1 = 999
n2 = 999
currentMax = 0
while n1 > 0:
    while n2 > 0:
        product = n1 * n2
        if product > currentMax:
            if is_palindrom(str(product)):
                currentMax = product
                print("new max", product, "=", n1, "x", n2)
        else:
            # we can skip all remaining n2 values as their product with n1
            #  will always be smaller than currentMax.
            break
        n2 -= 1
    n1 -= 1
    n2 = n1
