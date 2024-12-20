# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.dfs(root.left, root.right, 0)
        return root

    def dfs(self, left, right, level):
        if left is None or right is None:
            return
        if level % 2 == 0:
            temp = left.val
            left.val = right.val
            right.val = temp
            
        self.dfs(left.left, right.right, level + 1)
        self.dfs(left.right, right.left, level + 1)
        