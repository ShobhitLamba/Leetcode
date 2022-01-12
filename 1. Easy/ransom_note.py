class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag, count_rn = Counter(magazine), Counter(ransomNote)

        for k, v in count_rn.items():
            if count_mag[k] < v:
                return False

        return True    
