class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            res += 1
        return res
