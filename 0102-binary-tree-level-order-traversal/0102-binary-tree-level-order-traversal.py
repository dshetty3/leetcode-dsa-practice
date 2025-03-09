# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = [] #result
        q = deque([root]) # create a ques
        # q.append(root) #first add the root node to the ques

        while q: #when que is not null
            
            level = [] # in result
            for i in range(len(q)): 
                node = q.popleft() #root will be poped first # 1st level
                if node: # if it is a node
                    level.append(node.val) # add to level
                    q.append(node.left) #add its left cild and right child to the queue
                    q.append(node.right)

            if level: #if level not empty
                res.append(level) #add level to res
        return res
        