class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        eligible_nums = { '9': '6', '6': '9', '8': '8', '1': '1', '0': '0'}
        num, l, i = list(num), len(num), 0

        while i <= l // 2:
            if num[i] not in eligible_nums or eligible_nums[num[i]] != num[~i]:
                return False
            i += 1

        return True
            
