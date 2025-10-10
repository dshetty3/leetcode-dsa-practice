class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """

        n = len(energy)
        res = float('-inf')

        for i in range(n - k, n):
            total = 0
            j = i
            while j >=0:
                total += energy[j]
                res = max(res, total)
                j -= k
        return res
        