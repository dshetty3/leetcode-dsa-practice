class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        sol = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return res
        