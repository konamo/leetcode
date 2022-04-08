# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        m = 0
        def dfs(root):
            nonlocal m

            if not root:
                return 0

            a = dfs(root.left)
            b = dfs(root.right)
            
            m = max(m, a + b)
            return max(a, b) + 1

        dfs(root)
        return m






