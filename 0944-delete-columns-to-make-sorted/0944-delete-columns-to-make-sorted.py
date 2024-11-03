class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        m = len(strs)
        n = len(strs[0])
        count = 0

        for i in range(n):
            for j in range(1, m):
                if strs[j][i] < strs[j - 1][i]:
                    count += 1
                    break
        return count
        