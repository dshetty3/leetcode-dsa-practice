class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0 and curr != self.right:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        next = self.left.next
        prev = self.left

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next = self.right 
        prev = self.right.prev

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node = ListNode(val)
            next = curr
            prev = curr.prev

            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
        
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index == 0:
            next = curr.next
            prev = curr.prev

            next.prev = prev
            prev.next = next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)