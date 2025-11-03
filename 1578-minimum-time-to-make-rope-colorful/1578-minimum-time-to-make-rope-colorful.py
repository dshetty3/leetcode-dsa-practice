class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """

        res = 0
        n = len(colors)

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                res += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return res
        