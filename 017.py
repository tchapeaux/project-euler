import math

wordDict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def intToWord(n):
    assert n <= 999999
    word = ""
    thousands = math.floor(n / 1000)
    if thousands > 0:
        word += intToWord(thousands)
        word += " thousand"
    n2 = n - thousands * 1000
    assert n2 < 1000
    hundreds = math.floor(n2 / 100)
    if hundreds > 0:
        if thousands > 0:
            word += " "
        word += intToWord(hundreds)
        word += " hundred"
    n3 = n2 - hundreds * 100
    assert n3 < 100
    if n3 > 0:
        if hundreds > 0 or thousands > 0:
            word += " and "
        dozens = math.floor(n3 / 10)
        if dozens < 2:
            word += wordDict[n3]
        else:
            units = n3 - dozens * 10
            word += wordDict[dozens * 10]
            if units > 0:
                word += "-"
                word += wordDict[units]
    return word

assert intToWord(2532) == "two thousand five hundred and thirty-two"
assert intToWord(342) == "three hundred and forty-two"
assert intToWord(115) == "one hundred and fifteen"


def letterCount(word):
    # note: as requested, we do not count spaces and hyphens
    count = 0
    for char in word:
        if char not in [" ", "-"]:
            count += 1
    return count


assert letterCount(intToWord(342)) == 23
assert letterCount(intToWord(115)) == 20


N = 1000
theSum = 0
for i in range(1, N + 1):
    word = intToWord(i)
    theSum += letterCount(word)
print(theSum)
