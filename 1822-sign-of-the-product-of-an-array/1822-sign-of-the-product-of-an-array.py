class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        neg = 0
        product = 1

        for n in nums:
            if n < 0:
                neg += 1
        
        for i in range(len(nums)):
            product *= nums[i]
        
        if neg % 2 == 0 and product:
            return 1
        elif neg % 2 == 1 and product:
            return -1
        else:
            return 0

        