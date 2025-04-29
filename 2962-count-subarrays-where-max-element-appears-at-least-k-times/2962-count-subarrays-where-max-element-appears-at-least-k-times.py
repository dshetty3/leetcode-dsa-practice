class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

        max_element = max(nums)

        res = 0
        l = 0
        max_element_window = 0

        for r in range(len(nums)):
            if nums[r] == max_element:
                max_element_window += 1

            while max_element_window == k:
                if nums[l] == max_element:
                    max_element_window -= 1
                l += 1
            res += l
        return res