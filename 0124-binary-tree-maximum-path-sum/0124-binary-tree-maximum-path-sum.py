# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        sum = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            sum[0] = max(sum[0], node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return sum[0]        