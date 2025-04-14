class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.left.next.val
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.right.prev.val
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.left.next == self.right
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()