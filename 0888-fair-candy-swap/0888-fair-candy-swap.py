class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """

        diff = ( sum(aliceSizes) - sum(bobSizes) ) // 2
        s = set(aliceSizes)

        for b in bobSizes:
            if b + diff in s:
                return [b + diff, b]
        