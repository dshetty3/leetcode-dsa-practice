# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        arr = []

        def dfs(node):
            if not node: return

            dfs(node.left)
            nonlocal prev
            if prev is not None and prev.val > node.val:
                if not arr:
                    arr.append(prev)
                    arr.append(node)
                else:
                    arr[1] = node
            prev = node
            dfs(node.right)
        dfs(root)

        assert(len(arr) == 2)
        arr[0].val, arr[1].val = arr[1].val, arr[0].val  
        