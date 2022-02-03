# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        self.inorder(root, l)
        left, right = 0, len(l) - 1

        while left < right:
            sum = l[left] + l[right]
            if sum == k:
                return True
            elif sum < k:
                left += 1
            else:
                right -= 1

        return False

    def inorder(self, node, l):
        if not node:
            return

        self.inorder(node.left, l)
        l.append(node.val)
        self.inorder(node.right, l)
