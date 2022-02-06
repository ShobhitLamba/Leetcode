class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        cnt = 0

        for word in words:
            good = True
            for letter in word:

                if word.count(letter) > c[letter]:
                    good = False
                    break

            if good:
                cnt += len(word)

        return cnt
