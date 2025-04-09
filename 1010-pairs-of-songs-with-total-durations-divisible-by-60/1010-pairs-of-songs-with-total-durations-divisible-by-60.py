class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """

        count = defaultdict(int)
        pairs = 0

        for t in time:
            if not (t % 60):
                pairs += count[0]
            else:
                pairs += count[60 - (t % 60)]
            count[t % 60] += 1
        return pairs





        return pairs
        