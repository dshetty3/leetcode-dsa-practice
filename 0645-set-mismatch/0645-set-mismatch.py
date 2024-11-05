class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        n = Counter(nums)
        d, m = 0,0
        for i in range(1, len(nums) + 1):
            if n[i] == 2:
                d = i
            elif n[i] == 0:
                m = i
        return [d,m]

        
        