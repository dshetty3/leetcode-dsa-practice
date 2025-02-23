class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        # n = len(nums)
        # cur_sum = 0

        # for i in range(k):
        #     cur_sum += nums[i]

        # max_avg = float(cur_sum) / k

        # for i in range(k, n):
        #     cur_sum += nums[i]
        #     cur_sum -= nums[i - k]

        #     avg = float(cur_sum) / k
        #     max_avg = max(max_avg, avg)

        # return max_avg

        l = 0
        r = 0
        curr_sum = 0
        max_sum = float('-inf')

        while r < len(nums):
            curr_sum += nums[r]
        
            if r - l + 1 == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[l]
                l += 1
            r += 1
        return float(max_sum)/ k

        

        