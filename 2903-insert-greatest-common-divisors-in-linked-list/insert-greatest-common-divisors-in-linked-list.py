# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a,b):
            while b > 0:
                a, b = b, a % b
            return a

        prev = head
        cur = head.next
        
        while cur:
            res = gcd(cur.val, prev.val)
            g = ListNode(res)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next

        return head
        