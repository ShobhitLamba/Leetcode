class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        shortest = min(strs, key=len) # min returns the str, not len of it
        zipped = zip(*strs)

        for idx, z in enumerate(zipped):
            if all(l == shortest[idx] for l in z):
                count += 1
            else: # return if chars dont match with shortest len word
                break

        return shortest[:count]
