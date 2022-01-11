class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd, even = 0, 0

        for k, v in count.items():
            odd += v % 2

        return True if odd in [0,1] else False    
