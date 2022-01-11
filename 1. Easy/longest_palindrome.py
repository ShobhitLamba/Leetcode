class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(list(s))
        even, odd = 0, 0
        for k, v in count.items():
            even += v // 2
            odd += v % 2

        return (even * 2) + min(1, odd)
            
