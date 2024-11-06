# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        res = None

        while stack1 or stack2 or carry:
            summ = carry

            if stack1: summ += stack1.pop()
            if stack2: summ += stack2.pop()

            node = ListNode(summ % 10)
            node.next = res
            res = node

            carry = summ // 10
        return res



        