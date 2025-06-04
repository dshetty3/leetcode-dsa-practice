class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        

        n = len(word)
        res = ""
        length = n - numFriends + 1
        max_char = max(word)

        for i in range(n):
            if word[i] == max_char:
                substr = word[i: i + length]
                res = max(res, substr)
        return res
            
        