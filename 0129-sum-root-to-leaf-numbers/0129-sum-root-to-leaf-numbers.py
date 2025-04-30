# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        q = deque()
        res = 0
        if root:
            q.append(root)

        while q:
            node = q.popleft()
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val * 10
                q.append(node.left)
            if node.right:
                node.right.val += node.val * 10
                q.append(node.right)
        return res   
        