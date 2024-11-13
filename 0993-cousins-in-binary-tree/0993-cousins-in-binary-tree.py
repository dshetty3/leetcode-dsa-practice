# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            x_found, y_found = False, False
            for i in range(size):
                curr = q.popleft()

                if curr.val == x:
                    x_found = True
                if curr.val == y:
                    y_found = True
                if curr.left is not None and curr.right is not None:
                    if (curr.left.val == x and curr.right.val == y) or (curr.left.val == y and curr.right.val == x):
                        return False
                
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                
            
            if x_found and y_found:
                return True
            if x_found and y_found:
                return False
                
        return False

        
        