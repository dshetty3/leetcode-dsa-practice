class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """

        for i in range(k - 1):
            colors.append(colors[i])
        

        l = 0
        r = 1
        res = 0

        while r < len(colors):
            if colors[r] == colors[r - 1]:
                l = r
                r += 1
                continue
            r += 1

            if r - l < k: continue

            res += 1
            l += 1
        return res
        