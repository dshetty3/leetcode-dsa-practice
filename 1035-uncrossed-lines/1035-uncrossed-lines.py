class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        dp = {}

        def dfs(i, j):
            if i <= 0 or j <= 0:
                return 0
            
            if (i,j) in dp:
                return dp[(i, j)]
            
            if nums1[i - 1] == nums2[j - 1]:
                dp[(i, j)] = 1 + dfs(i - 1, j - 1)
            else:
                dp[(i, j)] = max(dfs(i - 1, j), dfs(i, j - 1))
            
            return dp[(i, j)]
        
        return dfs(len(nums1), len(nums2))
                