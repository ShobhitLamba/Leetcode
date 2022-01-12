class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        l, r = 2, num // 2

        while l <= r:
            m = l + (r - l) // 2
            guess = m * m
            if guess == num:
                return True
            if guess < num:
                 l = m + 1
            else:
                r = m - 1

        return False
