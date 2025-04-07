class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        if total % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        target = total // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False

        # nums.sort(reverse=True)

        # def backtrack(start, curr_sum):
        #     if curr_sum == target:
        #         return True
        #     if curr_sum > target:
        #         return False
            
        #     for i in range(start, len(nums)):
        #         if backtrack(i + 1, curr_sum + nums[i]):
        #             return True
        #     return False
        
        # return backtrack(0,0)
        