class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        ans = haystack.split(needle)[0]

        return len(ans) if len(ans) != len(haystack) else -1
