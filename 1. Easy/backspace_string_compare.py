class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            stack = []
            for c in string:
                if c == '#':
                    popped = stack.pop() if stack else c
                else:
                    stack.append(c)
            print(stack)
            return stack

        return helper(s) == helper(t)
        
