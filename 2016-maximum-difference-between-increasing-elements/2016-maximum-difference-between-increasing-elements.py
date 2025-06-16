class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        pre = nums[0]
        n = len(nums)


        for i in range(1, n):
            if nums[i] > pre:
                ans = max(ans, nums[i] - pre)
            else:
                pre = nums[i]
        return ans 


        