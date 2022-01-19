class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(number):
            total = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total += digit ** 2

            return total

        slow, fast = n, helper(n)
        while fast != 1 and slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))

        return fast == 1
