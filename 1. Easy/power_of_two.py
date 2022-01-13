class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Method 1 with bit trick
        #if n == 0:
        #    return False
        #
        #return n & (-n) == n

        #Method 2 normal division
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2

        return True
