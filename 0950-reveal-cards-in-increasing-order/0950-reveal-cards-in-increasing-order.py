class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        q = deque()

        for i in range(len(deck)):
            q.append(i)
        
        deck.sort()
        res = [0] * len(deck)

        for card in deck:
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())
        
        return res
