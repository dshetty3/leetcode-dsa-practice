class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        sol = []

        def backtrack(i, currSum):
            if len(sol) == k and currSum == n:
                res.append(sol[:])
                return
            
            elif len(sol) > k and currSum != n:
                return
            
            for j in range(i, 10):

                sol.append(j)
                backtrack( j + 1, currSum + j)
                sol.pop()

        backtrack(1, 0)
        return res
            
        