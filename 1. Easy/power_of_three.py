class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        #Method 1 with integer limitation trick
        #return n > 0 and 1162261467 % n == 0

        #Method 2 normal division
        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3

        return True
