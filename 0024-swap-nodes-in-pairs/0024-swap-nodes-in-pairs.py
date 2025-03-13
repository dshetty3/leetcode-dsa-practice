# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            fast = curr.next.next
            slow = curr.next

            curr.next = fast
            slow.next = curr
            prev.next = slow

            prev = curr
            curr = fast
        return dummy.next
        