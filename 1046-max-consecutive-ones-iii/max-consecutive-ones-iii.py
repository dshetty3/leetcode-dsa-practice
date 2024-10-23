class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_w = 0
        nums_z = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                nums_z += 1
            
            while nums_z > k:
                if nums[l] == 0:
                    nums_z -= 1
                l += 1
            
            w = (r - l) + 1
            max_w = max(max_w, w)

        return max_w

        