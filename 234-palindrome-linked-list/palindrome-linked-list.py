# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(N) - space
        # nums = []

        # while head:
        #     nums.append(head.val)
        #     head = head.next
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1    
        # return True

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2 -> 3 -> 3 -> 2 
        #     s -> prev
        #     temp = 3

        prev = None
        #slow reaches last node
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


        


        
        