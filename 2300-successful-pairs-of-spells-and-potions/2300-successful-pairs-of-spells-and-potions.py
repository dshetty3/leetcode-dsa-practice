class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        potions.sort()
        res = []

        for s in spells:
            l = 0
            r = len(potions) -1
            idx = len(potions)

            while l <= r:
                m = (l+r) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            res.append(len(potions) - idx)
        return res
        