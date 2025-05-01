# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.count = 0

        def dfs(node):
            if node:
                self.count += 1
                dfs(node.left)
                dfs(node.right)
            else:
                return
        
        dfs(root)
        return self.count