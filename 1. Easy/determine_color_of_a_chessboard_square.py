class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        ref = {1: ['a','c','e','g'], 0:['b','d','f','h']}

        if coordinates[0] in ref[0]:
            a = 0
        else:
            a = 1

        return True if (a + int(coordinates[1])) % 2 == 1 else False
