class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []

        for word, cnt in count.items():
            heappush(heap, (-cnt, word))

        return [heappop(heap)[1] for _ in range(k)]
