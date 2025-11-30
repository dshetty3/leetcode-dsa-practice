class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        remain_index = { 0: -1 }

        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_index:
                length = i - remain_index[prefix]
                res = min(res, length)
            remain_index[cur_sum] = i
        return -1 if res == len(nums) else res        