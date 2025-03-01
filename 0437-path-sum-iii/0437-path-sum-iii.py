# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        def dfs(node, currSum):
            if not node:
                return 
            res = 0
            if currSum == targetSum:
                res += 1
            if node.left:
                res += dfs(node.left, currSum + node.left.val)
            if node.right:
                res += dfs(node.right, currSum + node.right.val)
            return res
                
        if not root: return 0
        return dfs(root, root.val) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

        

             
            
            
        