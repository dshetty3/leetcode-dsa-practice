class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0

        for n in nums:
            length = len(str(n))
            if length % 2 == 0:
                count += 1
        return count
            
        