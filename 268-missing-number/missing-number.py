class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashSet = set(nums)

        for n in range(len(nums) + 1):
            if n not in hashSet:
                return n

        