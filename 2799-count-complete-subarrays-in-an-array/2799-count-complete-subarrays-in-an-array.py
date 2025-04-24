class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = len(set(nums))
        cntMap = {}
        res = 0
        l = 0

        for i in range(len(nums)):
            cntMap[nums[i]] = cntMap.get(nums[i], 0) + 1
            while len(cntMap) == d:
                res += len(nums) - i
                cntMap[nums[l]] -= 1
                if cntMap[nums[l]] == 0:
                    del cntMap[nums[l]]
                l += 1
        return res
        