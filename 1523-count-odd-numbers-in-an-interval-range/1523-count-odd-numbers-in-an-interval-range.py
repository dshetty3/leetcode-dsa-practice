class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        # count = 0

        # for i in range(low, high + 1):
        #     if (i % 2) == 1:
        #         count += 1
        # return count

        length = high - low + 1
        count = length // 2

        if length % 2 and low % 2:
            count += 1
        return count

        