# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        def helper(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            return (
                helper(list_node.next, tree_node.left) or 
                helper(list_node.next, tree_node.right)) 
            # either the linkedlist will be in left side of node or right hence or function
        if helper(head, root):
            return True
                #if there is head and root present
        if not root:
            return False
                # null pointer
        return(self.isSubPath(head,root.left) or
                self.isSubPath(head,root.right))

