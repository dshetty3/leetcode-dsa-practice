class ListNode:
    def __init__(self, val = 0, prev = None, next =None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next = node.next
            prev = node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)
    
    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.count = 0
        self.valMap = {} #key -> val
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.count and self.listMap[cnt].length() == 0:
            self.count += 1


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap == 0: return

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.count].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.counter(key)
        self.count = min(self.count, self.countMap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)