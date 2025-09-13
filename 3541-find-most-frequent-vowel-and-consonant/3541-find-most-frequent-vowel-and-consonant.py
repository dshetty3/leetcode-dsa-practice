class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = Counter(s)
        vowel = 0
        consonent = 0

        for c, count in freq.items():
            if c in 'aeiou':
                vowel = max(vowel, count)
            else:
                consonent = max(consonent, count)
        
        return vowel + consonent


        