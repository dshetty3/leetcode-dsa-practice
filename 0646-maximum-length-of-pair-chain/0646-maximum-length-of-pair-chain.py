class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        pairs.sort(key = lambda p:p[1])
        count = 1
        end = pairs[0][1]

        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                count += 1
                end = pairs[i][1]
        return count

        