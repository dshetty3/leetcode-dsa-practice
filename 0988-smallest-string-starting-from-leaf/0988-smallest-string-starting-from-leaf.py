# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """

        q = deque()
        res_string = ''

        q.append([root, chr(root.val + ord('a'))])
        while q:
            node, curr_string = q.popleft()
            if not node.left and not node.right:
                res_string = min(res_string, curr_string) if res_string else curr_string
            if node.left:
                q.append([node.left, chr(node.left.val + ord('a')) + curr_string])
            
            if node.right:
                q.append([node.right, chr(node.right.val + ord('a')) + curr_string])

        return res_string
        