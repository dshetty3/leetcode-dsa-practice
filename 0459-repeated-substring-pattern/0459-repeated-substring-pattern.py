class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s[1:] + s[:-1]

        if s in ss:
            return True
        else:
            return False

        

        

        
        