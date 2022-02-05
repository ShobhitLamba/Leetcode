class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""

        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title += chr(remainder + ord('A'))

        return title[::-1]
            
