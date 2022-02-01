# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        q = [[root]]

        for elem in q:
            record = []

            for c in elem:
                if c.left: record.append(c.left)
                if c.right: record.append(c.right)

            if record:
                q.append(record)

        values = [[x.val for x in sublist] for sublist in q]

        return [sum(v) / len(v) for v in values]
