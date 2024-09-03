# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # need to read the values of the node from left to right
        #so 1,3,2
        res=[]
        self.Traversal(root, res)
        return res


    def Traversal (self, root, res):
        if root is not None:
            self.Traversal(root.left, res)
            res.append(root.val)
            self.Traversal(root.right,res)
        