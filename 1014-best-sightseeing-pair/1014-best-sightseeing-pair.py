class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """

        res = 0
        curr_max = values[0] - 1

        for i in range(1, len(values)):
            res = max(res, values[i] + curr_max)
            curr_max = max(curr_max - 1, values[i] - 1)
        return res


        