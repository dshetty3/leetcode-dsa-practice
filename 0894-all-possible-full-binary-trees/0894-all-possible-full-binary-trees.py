# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """

        dp = {}

        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n):
                r = n - 1 - l

                leftTree = backtrack(l)
                rightTree = backtrack(r)

                for t1 in leftTree:
                    for t2 in rightTree:
                        res .append(TreeNode(0, t1, t2))
        
            dp[n] = res
            return res

        return backtrack(n)

        