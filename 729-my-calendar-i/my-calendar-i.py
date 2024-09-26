class MyCalendar(object):

    def __init__(self):
        self.event = []        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        for s, e in self.event:
            if (e > start and end > s):
                return False
        self.event.append((start,end))
        return True


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)