# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        queue = deque([root])
        values = []


        while queue:
            node = queue.popleft()
            values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        values.sort()

        new_root = TreeNode(values[0])
        curr_node = new_root

        for val in values[1:]:
            curr_node.right = TreeNode(val)
            curr_node = curr_node.right

        return new_root        