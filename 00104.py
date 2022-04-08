# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0
        def dfs(node):
            nonlocal m

            if not node:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
            m = max(m, left, right)
            return max(left, right) + 1


        dfs(root)
        return m
