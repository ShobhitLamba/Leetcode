class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros, ones = s.split("1"), s.split("0")
        z, o = len(max(zeros, key = len)), len(max(ones, key = len))

        return o > z
