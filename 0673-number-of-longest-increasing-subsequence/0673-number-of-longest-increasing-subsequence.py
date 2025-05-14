class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if res[j] + 1 > res[i]:
                        res[i] = res[j] + 1
                        count[i] = 0
                    
                    if res[j] + 1 == res[i]:
                        count[i] += count[j]
        
        max_l = max(res)
        result = 0

        for i in range(len(nums)):
            if res[i] == max_l:
                result += count[i]
        return result

        