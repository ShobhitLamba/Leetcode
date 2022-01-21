class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for idx in range(len(word)):
            if word[idx] == ch:
                return word[:idx + 1][::-1] + word[idx + 1:]

        return word
