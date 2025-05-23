"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, d = stack.pop()
            max_depth = max(max_depth, d)
            for child in node.children:
                stack.append((child, d + 1))
        
        return max_depth