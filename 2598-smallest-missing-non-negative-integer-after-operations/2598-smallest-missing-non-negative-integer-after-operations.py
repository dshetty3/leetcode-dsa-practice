class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """

        map = Counter(n % value for n in nums)
        res = 0
        while map[res % value] > 0:
            map[res % value] -= 1
            res += 1
        return res
        