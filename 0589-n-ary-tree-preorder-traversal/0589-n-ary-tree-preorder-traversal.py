"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def dfs(root, ans):
            if not root:
                return None
            ans.append(root.val)
            for child in root.children:
                dfs(child, ans)
            return ans

        return dfs(root,[])

        


        


        