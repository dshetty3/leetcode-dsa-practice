class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """

        diff = [0] * (len(nums) + 1)

        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        
        for i in range(1, len(nums)):
            diff[i] += diff[i - 1]
        
        for i in range(len(nums)):
            if nums[i] > diff[i]:
                return False
        return True
        