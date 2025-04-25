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
        :rtype: List[List[int]]
        """

        if not root: return []

        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, currSum, leaves = queue.pop()
            if not curr.left and not curr.right and currSum == targetSum:
                res.append(leaves)
            
            if curr.left:
                queue.append((curr.left, currSum + curr.left.val, leaves + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, currSum + curr.right.val, leaves + [curr.right.val]))
        
        return res
        