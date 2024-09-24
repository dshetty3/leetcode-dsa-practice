class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        close = nums[0]

        for n in nums:
            if abs(n) < abs(close):
                close = n
        
        if close < 0 and abs(close) in nums:
            return abs(close)
        else:
            return close
        