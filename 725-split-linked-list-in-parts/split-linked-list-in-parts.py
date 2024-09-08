# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        #find length of linkedList

        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        #find length of subarray and the number of extra nodes
        base_length, remainder = length // k, length % k
        curr = head
        res = []

        for i in range(k):
            res.append(curr)

            for j in range(base_length - 1 + (1 if remainder else 0)):
                if not curr: break
                curr = curr.next
            remainder -= (1 if remainder else 0)
            if curr:
                
                curr.next, curr = None, curr.next 
        return res 
        