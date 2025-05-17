class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k <= 1:
            return 0
        
        count = 0
        total = 1
        l = 0

        for r in range(len(nums)):
            total *= nums[r]

            while total >= k:
                total //= nums[l]
                l += 1
            
            count += (r - l + 1)
        
        return count
        