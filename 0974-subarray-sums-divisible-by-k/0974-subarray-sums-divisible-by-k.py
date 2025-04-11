class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        curr_sum = 0
        prefix_sum = { 0 : 1 }
        res = 0

        for n in nums:
            curr_sum += n
            remainder = curr_sum % k
            if remainder in prefix_sum:
                res += prefix_sum.get(remainder, 0)
            prefix_sum[remainder] = 1 + prefix_sum.get(remainder, 0) 
        return res



        