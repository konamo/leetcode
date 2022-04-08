# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        found = False
        ret = None
        
        def dfs(node):
            nonlocal found
            
            if not node:
                return
            
            if found:
                return

            if node.val == val:
                found = True
                ret = node
            elif node.val > val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)
        return ret

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        while current_node != None:
            if current_node.val == val:
                return current_node
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None        
