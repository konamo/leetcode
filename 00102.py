# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = []    

        def bfs(root):
            search_list = [root]

            while search_list:
                length = len(search_list)
                ret.append([])

                for ii in range(length):
                    node = search_list.pop(0)
                    ret[-1] += [node.val]
                    if node.left:
                        search_list.append(node.left)
                    if node.right:
                        search_list.append(node.right)
                        
        bfs(root)
        return ret
