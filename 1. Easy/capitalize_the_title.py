class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def capitalize(word):
            if len(word) <= 2:
                return word

            return word[:1].upper() + word[1:]

        title = title.lower().split()
        title = [capitalize(word) for word in title]

        return " ".join(title)
