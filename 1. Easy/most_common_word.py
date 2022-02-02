class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized.split()

        w_count = defaultdict(int)
        banned = set(banned)

        for word in words:
            if word not in banned:
                w_count[word] += 1

        return max(w_count, key = w_count.get)
                             
