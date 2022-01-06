class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s.lower() if char.isalnum()])
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

        
