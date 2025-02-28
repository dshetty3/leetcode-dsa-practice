class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        senate = list(senate)
        R = deque()
        D = deque()

        for i, n in enumerate(senate):
            if n == 'D':
                D.append(i)
            else:
                R.append(i)
        
        while D and R:
            dsenate = D.popleft()
            rsenate = R.popleft()

            if rsenate < dsenate:
                R.append(rsenate + len(senate))
            else:
                D.append(dsenate + len(senate))
        return "Radiant" if R else "Dire"
        