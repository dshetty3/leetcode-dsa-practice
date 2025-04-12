class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        res = []
        count = Counter(nums)

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in count:
                if count[n] > 0:
                    sol.append(n)
                    count[n] -= 1

                    backtrack()

                    count[n] += 1
                    sol.pop()
        backtrack()
        return res
            
            
        