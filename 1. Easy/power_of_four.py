class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        #Method 1 with log trick
        #return n > 0 and math.log2(n) % 2 == 0

        #Method 2 normal division
        if n <= 0:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n = n // 4

        return True
