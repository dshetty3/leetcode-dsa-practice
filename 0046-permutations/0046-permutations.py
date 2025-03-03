class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        res = []
        sol = []

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res

        