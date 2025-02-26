class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """


        print(max(candies))
        res = []

        for c in candies:
            if c + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res 
