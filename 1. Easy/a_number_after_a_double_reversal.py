class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(num):
            ans = 0
            while num > 0:
                ans = ans * 10 + num % 10
                num = num // 10

            return ans

        reversed1 = reverse(num)
        reversed2 = reverse(reversed1)

        return num == reversed2
