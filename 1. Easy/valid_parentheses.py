class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char in valid:
                top = stack.pop() if stack else '#'
                if top != valid[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
