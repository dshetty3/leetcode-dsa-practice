class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = 0
        self.capacity = k
        self.left = None
        self.right = None
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        if self.left is None:
            self.left = ListNode(value, None, None)
            self.right = self.left
        else:
            self.left.prev = ListNode(value, self.left, None)
            self.left = self.left.prev

        self.size += 1
        return True 
        
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        if self.left is None:
            self.left = ListNode(value, None, None)
            self.right = self.left
        else:
            self.right.next = ListNode(value, None, self.right)
            self.right = self.right.next
        
        self.size += 1
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.left = None
            self.right = None
        else:
            self.left = self.left.next
        
        self.size -= 1
        return True

    
    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.left = None
            self.right = None
        else:
            self.right = self.right.prev

        self.size -= 1
        return True 
        

    def getFront(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.left.val
        

    def getRear(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.right.val
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()