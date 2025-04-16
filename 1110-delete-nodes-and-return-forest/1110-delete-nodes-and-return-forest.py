# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        res = []

        def dfs(node, is_root):
            if not node: return None

            deleted = node.val in to_delete
            if is_root and not deleted:
                res.append(node)
            
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return node if not deleted else None
        
        dfs(root, True)
        return res




        


        