class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bitwise AND of same number will be same
        # Bitwiase and of smalled number and bigger will lead to smaller than the bigger number i.e. 2 & 3 = 2
        target = max(nums)
        size, res = 0, 0
        for n in nums:
            if n == target:
                size += 1
            else:
                size = 0
            res = max(res, size)
        return res
