import datetime

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


def asString(weekday_int):
    return weekdays[weekday_int]

day = datetime.date(1901, 1, 1)
print(day)
print(day.weekday(), asString(day.weekday()))

firstSundayCount = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        day = datetime.date(year, month, 1)
        if day.weekday() == 6:  # Sunday
            firstSundayCount += 1

print(firstSundayCount)
