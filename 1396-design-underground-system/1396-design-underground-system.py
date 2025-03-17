class UndergroundSystem(object):

    def __init__(self):
        self.checkInMap = {}
        self.totalMap = {}
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """

        self.checkInMap[id] = (stationName, t)
    
    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start, time = self.checkInMap[id]

        route = (start, stationName)
        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]
        self.totalMap[route][0] += t - time
        self.totalMap[route][1] += 1
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        total, count = self.totalMap[(startStation, endStation)]
        return float(total) / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)