class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        S = list(S)
        for i in S:
            if i in J:
                count += 1

        return count
