class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        words = sentence.split()
        if len(words) == 1:
            if words[0][0] != words[0][-1]:
                return False
                
        for c in range(len(words) - 1):
            if words[c][-1] != words[c+1][0]:
                return False
            
            if words[0][0] != words[-1][-1]:
                return False
            

        return True
        