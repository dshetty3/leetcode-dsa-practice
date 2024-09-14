class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if n and curr_max equal, n & curr_max = curr_max
        # if n < curr_max, n & curr_max < curr_max
        # if n > curr_max, n & curr_max < curr_max



        # target = max(nums)
        # size, res = 0, 0
        # for n in nums:
        #     if n == target:
        #         size += 1
        #     else:
        #         size = 0
        #     res = max(res, size)
        # return res


        size, res = 0, 0
        curr_max = 0
        res = 0
        for n in nums:
            if n > curr_max:
                curr_max = n
                size = 1
                res = 0
            elif n == curr_max:
                size += 1
            else:
                size = 0 
            res = max(size, res)       
        return res

