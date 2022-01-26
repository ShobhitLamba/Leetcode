class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0, 1, 1

        if n == 0:
            return first
        elif n == 1:
            return second
        elif n == 2:
            return third
        else:
            for i in range(3, n + 1):
                first, second, third = second, third, first + second + third

        return third
        
