# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        ans = []
        stack = []
        cnt = 0

        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                cnt_val, val = stack.pop()
                ans[cnt_val] = head.val

            
            stack.append([cnt, head.val])
            cnt += 1
            head = head.next

        return ans



        