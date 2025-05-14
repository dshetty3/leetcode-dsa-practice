# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node, minVal, maxVal):
            if not node:
                return maxVal - minVal
            

            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            left_diff = dfs(node.left, minVal, maxVal)
            right_diff = dfs(node.right, minVal, maxVal)

            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)
            

        