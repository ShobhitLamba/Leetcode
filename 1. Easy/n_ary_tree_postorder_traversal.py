"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack, ans = [root], []

        while stack:
            root = stack.pop()
            if root is not None:
                ans.append(root.val)
            for c in root.children:
                stack.append(c)

        return ans[::-1]
