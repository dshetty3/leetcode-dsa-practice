class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        res = 0
        empty = 0
        

        while numBottles > 0:
            res += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        return res
        