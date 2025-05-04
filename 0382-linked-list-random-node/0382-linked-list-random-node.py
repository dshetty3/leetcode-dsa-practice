# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()