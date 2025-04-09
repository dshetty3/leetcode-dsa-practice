class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = {}

        def dfs(i, k):
            if k == 1:
                return sum(nums[i:])
            if(i, k) in dp:
                return dp[(i,k)]
            

            curSum = 0
            res = float("inf")
            for j in range(i, len(nums) - k + 1):
                curSum += nums[j]
                maxSum = max(curSum, dfs(j + 1, k - 1))
                res = min(res, maxSum)
                if curSum > res:
                    break
            dp[(i, k)] = res
            return res
        return dfs(0, k)


