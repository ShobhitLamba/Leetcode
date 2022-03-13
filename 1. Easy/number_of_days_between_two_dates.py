class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2: date1, date2 = date2, date1
        y1, m1, d1 = [int(x) for x in date1.split("-")]
        y2, m2, d2 = [int(x) for x in date2.split("-")]

        leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        dates = 365*(y2 - y1) + sum(leap(y) for y in range(y1, y2))

        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        dates -= days[m1 - 1] + (m1 > 2 and leap(y1)) + d1
        dates += days[m2 - 1] + (m2 > 2 and leap(y2)) + d2

        return dates
