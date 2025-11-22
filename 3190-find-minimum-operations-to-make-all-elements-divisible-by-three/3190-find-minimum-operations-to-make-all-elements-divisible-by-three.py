class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0

        for num in nums:
            n = num % 3
            res += min(n, 3 - n)
        return res
