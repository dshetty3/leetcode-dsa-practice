class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """

        a = 0
        b = 0

        l = 0

        for r in range(len(colors)):
            if colors[l] != colors[r]:
                l = r
            extra = r - l + 1 - 2
            if extra > 0:
                if colors[r] == 'A':
                    a += 1
                if colors[r] == 'B':
                    b += 1
        return a > b

        