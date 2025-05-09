class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0 
        l = 0
        count = defaultdict(int)

        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


        