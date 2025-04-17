# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num_node = [0]

        def dfs(node):
            if not node: return (0, 0)

            N_left, left_sum = dfs(node.left)
            N_right, right_sum = dfs(node.right)

            n = 1 + N_left + N_right
            summ = node.val + left_sum + right_sum
            avg = summ / n

            if node.val == avg:
                num_node[0] += 1
            
            return(n, summ)
        
        dfs(root)
        return num_node[0]


        