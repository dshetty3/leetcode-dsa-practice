class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        counter = defaultdict(int)

        word = 'balloon'

        for c in text:
            if c in word:
                counter[c] += 1
            
        if any(c not in counter for c in word):
            return 0
            
        else:
            return min(counter['b'], 
                            counter['a'],
                            counter['l'] // 2,
                            counter['o'] // 2,
                            counter['n'])
        