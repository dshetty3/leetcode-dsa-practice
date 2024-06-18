class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """

        min1 = min2 = float("inf")

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
            
        leftover = money - min1 - min2
        return leftover if leftover >= 0 else money

        