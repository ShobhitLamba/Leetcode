# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return []

            return dfs(root.left) + [root.val] + dfs(root.right)

        res = dfs(root)

        def helper(root, nums):
            if len(nums) == 0:
                return

            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = helper(root.left, nums[:mid])
            root.right = helper(root.right, nums[mid + 1:])

            return root

        return helper(root, res)
