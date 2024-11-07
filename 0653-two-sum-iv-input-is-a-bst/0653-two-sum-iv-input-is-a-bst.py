# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """

        if not root:
            return False
        queue = deque([root])
        seen = set()

        while queue:
            curr = queue.popleft()
            if curr.val in seen:
                return True
            else:
                seen.add(k - curr.val)
                if curr.left : queue.append(curr.left)
                if curr.right : queue.append(curr.right)
        return False

        