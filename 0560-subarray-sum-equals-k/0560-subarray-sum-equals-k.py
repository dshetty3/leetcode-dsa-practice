class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        curr_sum = 0

        prefixSum = { 0: 1}

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            res += prefixSum.get(diff,0)
            prefixSum[curr_sum] = 1 +  prefixSum.get(curr_sum,0)
        return res

        