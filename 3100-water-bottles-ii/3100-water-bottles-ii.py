class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        res = numBottles
        empty = numBottles
        while empty >= numExchange:
            res += 1
            empty -= numExchange - 1
            numExchange += 1
        return res
        