# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None

        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root

        ind = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:ind + 2], post[:ind + 1])
        root.right = self.constructFromPrePost(pre[ind + 2:], post[ind + 1:-1])

        return root
