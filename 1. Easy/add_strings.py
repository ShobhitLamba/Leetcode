class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0

        for i, n in enumerate(reversed(num1)):
            n1 += int(n) * 10 ** i

        for i, n in enumerate(reversed(num2)):
            n2 += int(n) * 10 ** i

        return str(n1 + n2)

        
