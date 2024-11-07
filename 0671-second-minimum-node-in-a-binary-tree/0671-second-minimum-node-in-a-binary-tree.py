# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        firstMin = secondMin = float('inf')

        stack = [root]

        while stack:
            curr = stack.pop()
            if curr.val < firstMin:
                secondMin = firstMin
                firstMin = curr.val
            if firstMin < curr.val < secondMin:
                secondMin = curr.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return -1 if secondMin == float('inf') else secondMin


        