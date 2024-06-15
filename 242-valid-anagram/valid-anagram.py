class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        if Counter(s) == Counter(t):
            return True
        else:
            return False
        