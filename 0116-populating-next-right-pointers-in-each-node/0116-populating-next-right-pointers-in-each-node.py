"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root: 
            return None
        q = deque()
        q.append(root)

        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()

                if i < level - 1:
                    node.next = q[0]
                else:
                    node.next = None

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root