class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Method 1 using XOR
        #ch = 0
        #
        #for c in s:
        #    ch ^= ord(c)
        #
        #for c in t:
        #    ch ^= ord(c)
        #
        #return chr(ch)

        # Method 2 using ord sum-subtraction
        ch = 0
        for c in t:
            ch += ord(c)

        for c in s:
            ch -= ord(c)

        return chr(ch)
