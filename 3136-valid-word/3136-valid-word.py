class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        hasVowel = False
        hasCons = False

        if len(word) < 3:
            return False
        
        for c in word:
            if c.isalpha():
                if c.lower() in 'aeiou':
                    hasVowel = True
                else:
                    hasCons = True
            elif not c.isdigit():
                return False
        return hasVowel and hasCons


        