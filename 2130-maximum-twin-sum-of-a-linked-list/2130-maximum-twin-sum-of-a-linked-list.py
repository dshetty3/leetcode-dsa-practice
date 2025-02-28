# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next

        l = 0
        r = len(array) - 1
        max_twin = 0

        while l < r:
            sum_twin = array[l] + array[r]
            max_twin = max(sum_twin, max_twin)
            l += 1
            r -= 1
        return max_twin


