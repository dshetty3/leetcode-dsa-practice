class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1
        
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^=1
                nums[i + 2] ^=1
                res += 1
        return res if len(nums) == sum(nums) else -1
        