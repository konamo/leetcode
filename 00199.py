# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []


        def dfs(node):
            if node.right:
                dfs(node.right)

    def rightSideView(self, root):
        # Traverse the tree level by level and add the last value of each level to the view. 
        view = []
        if root:
            level = [root]

            while level:
                view += [level[-1].val]
                l = []
                for node in level:
                    for kid in (node.left, node.right):
                        if kid:
                            l += [kid]
                level = l
        return view




def main():
    s = Solution()
    root = [1,2,3,null,5,null,4]
    print("1: " + str(s.rightSideView(root)))

    root = [1,null,3]
    print("2: " + str(s.rightSideView(root)))

    root = []
    print("3: " + str(s.rightSideView(root)))
    return



if __name__ == '__main__':
    main()
