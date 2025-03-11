class RandomizedSet(object):

    def __init__(self):
        self.numMap = {}
        self.numArray = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        res =  val not in self.numMap
        if res:
            self.numMap[val] = len(self.numArray)
            self.numArray.append(val)
        return res
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res =  val in self.numMap
        if res:
            idx = self.numMap[val]
            lastIndex = self.numArray[-1]
            self.numArray[idx] = lastIndex
            self.numArray.pop()
            self.numMap[lastIndex] = idx
            del self.numMap[val]
        return res
        

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.numArray)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()