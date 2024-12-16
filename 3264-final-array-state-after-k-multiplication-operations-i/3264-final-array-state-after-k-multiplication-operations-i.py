class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """

        while k > 0:
            min_num = 0
            for n in range(len(nums)):
                if nums[n] < nums[min_num]:
                    min_num = n
            nums[min_num] *= multiplier
            k -= 1
        return nums


        