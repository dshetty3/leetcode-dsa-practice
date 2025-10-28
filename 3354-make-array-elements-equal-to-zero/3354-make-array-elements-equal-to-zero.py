class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        s = sum(nums)
        l = 0
        r = s
        for i in range(len(nums)):
            if nums[i] == 0:
                if 0 <= l - r <= 1:
                    res += 1
                if 0 <= r - l <= 1:
                    res += 1
            else:
                l += nums[i]
                r -= nums[i]
        return res
        