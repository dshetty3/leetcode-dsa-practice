class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        sol = []

        candidates.sort()
        
        def backtrack(i, total):
            if total == target:
                res.append(sol[:])
                return
            if total > target or i  == len(candidates): return

            sol.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i = i + 1
            backtrack(i + 1, total)

        backtrack(0,0)
        return res
        
