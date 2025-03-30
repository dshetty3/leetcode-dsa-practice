class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        while nums != [0] * len(nums):
            res += 1
            minimum = min([i for i in nums if i > 0])
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= minimum
        return res


        