# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        def dfs(node, parent):
            if not node:
                return None

            node.parent = parent
            node.done = False

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        #BFS - Start
        q = deque()
        q.append([target, 0])
        target.done = True
        ans = []
        while q:
            node, d = q.popleft()
            if d == k:
                ans.append(node.val)
            
            for nei in (node.left, node.right, node.parent):
                if nei is not None and not nei.done:
                    nei.done = True
                    q.append((nei, d + 1))
        return ans
