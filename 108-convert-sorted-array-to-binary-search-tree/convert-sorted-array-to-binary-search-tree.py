# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def BST (l,r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = BST(l,m - 1)
            root.right = BST(m + 1, r) 
            return root

        return BST(0, len(nums) - 1)       