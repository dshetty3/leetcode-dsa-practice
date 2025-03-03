# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """


        q = deque()
        q.append(root)
        max_sum = float('-inf')
        ans = 0
        level = 0

        while q:
            level += 1
            curr_sum = 0
            for n in range(len(q)):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if max_sum < curr_sum:
                max_sum = curr_sum
                ans = level

        return ans
            

                    
                
            
        
        
        