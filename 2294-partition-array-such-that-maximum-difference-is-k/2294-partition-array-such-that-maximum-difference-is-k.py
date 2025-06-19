class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        res = 1
        rec = nums[0]
        for n in nums:
            if n - rec > k:
                res += 1
                rec = n
        return res

        