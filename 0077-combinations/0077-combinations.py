class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        sol = []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            left = x
            need = k - len(sol)

            if left > need:    
                backtrack(x-1)
            sol.append(x)
            backtrack(x-1)
            sol.pop()
        
        backtrack(n)
        return res
        