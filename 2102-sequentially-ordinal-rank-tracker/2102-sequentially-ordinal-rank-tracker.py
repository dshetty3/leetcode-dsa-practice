class SORTracker(object):

    def __init__(self):
        self.list = SortedList()
        self.counter = 0
        

    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        self.list.add((-score, name))
        

    def get(self):
        """
        :rtype: str
        """

        ans = self.list[self.counter][1]
        self.counter += 1
        return ans
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()