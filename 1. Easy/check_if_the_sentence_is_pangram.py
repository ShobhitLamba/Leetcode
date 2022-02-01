class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [0] * 26

        for c in sentence:
            alphabets[ord(c) - 97] += 1

        for i in alphabets:
            if i == 0:
                return False

        return True
        
