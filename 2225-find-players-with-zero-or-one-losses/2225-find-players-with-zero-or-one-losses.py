class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = []
        losers = []
        tables = {}

        for w, l in matches:
            tables[w] = tables.get(w, 0)
            tables[l] = 1 + tables.get(l, 0)

        for k, v in tables.items():
            if v == 0:
                winners.append(k)
            if v == 1:
                losers.append(k)
        
        return [sorted(winners), sorted(losers)]


        