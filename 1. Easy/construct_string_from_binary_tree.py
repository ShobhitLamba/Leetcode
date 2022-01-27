# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, node: Optional[TreeNode]) -> str:
        if not node:
            return ""
        if node.left is None and node.right is None:
            return str(node.val)
        if node.right is None:
            return str(node.val) + "(" + self.tree2str(node.left) + ")"

        return str(node.val) + "(" + self.tree2str(node.left) + ")(" + self.tree2str(node.right) + ")"
