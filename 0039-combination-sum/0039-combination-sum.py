class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(candidates)
        res, sol = [], []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            if i == n or curr_sum > target:
                return
            
            backtrack(i + 1, curr_sum)

            sol.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            sol.pop()

        backtrack(0, 0)
        return res

        