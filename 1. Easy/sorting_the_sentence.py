class Solution:
    def sortSentence(self, s: str) -> str:
        word_order = [(word[-1], word[:-1]) for word in s.split()]
        word_order.sort(key = lambda x: x[0])

        return " ".join([word[1] for word in word_order])

        
