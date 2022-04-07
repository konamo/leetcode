# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = []
        direction = 1

        def bfs(root):
            nonlocal direction

            search_list = [root]

            while search_list:
                length = len(search_list)
                level = []

                for ii in range(length):
                    node = search_list.pop(0)
                    level.append(node.val)

                    if node.left:
                        search_list.append(node.left)
                    if node.right:
                        search_list.append(node.right)
                ret.append(level[::direction])
                direction *= -1
            return




        bfs(root)
        return ret
