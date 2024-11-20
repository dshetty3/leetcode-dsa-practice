class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = Counter(nums)

        for i in n:
            if n[i] > 1:
                return i
        