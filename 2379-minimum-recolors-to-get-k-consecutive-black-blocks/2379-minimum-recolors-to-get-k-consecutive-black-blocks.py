class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        l = 0
        white = 0
        recolor = float('inf')

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                white += 1

            if (r - l + 1) == k:
                recolor = min(recolor, white)
                if blocks[l] == 'W':
                    white -= 1
                l += 1

        return recolor
            



        