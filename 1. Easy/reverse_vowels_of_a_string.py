class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        while left <= right:
            if s[left] in "AEIOUaeiou" and s[right] in "AEIOUaeiou":
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            elif s[left] in "AEIOUaeiou":
                right -= 1

            else:
                left += 1

        return "".join(s)
