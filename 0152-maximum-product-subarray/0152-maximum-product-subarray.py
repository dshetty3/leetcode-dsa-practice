class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        
        res = nums[0]
        currMin, currMax = 1, 1

        # for i in range(len(nums)):
        #     curr = nums[i]
        #     res = max(curr, res)
        #     for j in range(i+1, len(nums)):
        #         curr *= nums[j]
        #         res = max(curr, res)
        
        # return res

        for num in nums:
            tmp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(tmp, num * currMin, num)
            res = max(res, currMax)
        return res





        