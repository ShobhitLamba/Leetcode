# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        ans = []

        q = deque([(root, None, 0)])

        while q:
            if len(ans) == 2:
                break
            node, parent, depth = q.popleft()
            if node.val == x or node.val == y:
                ans.append([parent, depth])
            if node.left:
                q.append((node.left, node, depth + 1))
            if node.right:
                q.append((node.right, node, depth + 1))

        n1, n2 = ans

        return n1[0] != n2[0] and n1[1] == n2[1]
    
