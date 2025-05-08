# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # stack = [root]
        # visit = [False]
        # res = []

        # while stack:
        #     curr = stack.pop()
        #     v = visit.pop()
        #     if curr:
        #         if v:
        #             res.append(curr.val)
        #         else:   #first goes the root, then right child and then left
        #             stack.append(curr)
        #             visit.append(True)
        #             stack.append(curr.right)
        #             visit.append(False)
        #             stack.append(curr.left)
        #             visit.append(False)
        # return res

        res = []

        def postorder(node):
            if not node:
                return None
            
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res

        