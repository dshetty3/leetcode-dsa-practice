class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        total = 0

        for n in range(len(timeSeries) - 1):
            total += min(timeSeries[n+1] - timeSeries[n], duration)
        return total + duration # for last item in list add duartion

        