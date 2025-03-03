class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        sol = []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            backtrack (i + 1)
            
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res