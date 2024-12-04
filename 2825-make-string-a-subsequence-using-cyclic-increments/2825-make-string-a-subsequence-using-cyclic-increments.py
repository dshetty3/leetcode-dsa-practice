class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """

        s2 = 0

        for s1 in range(len(str1)):
            if s2 < len(str2) and (
                str1[s1] == str2[s2] or
                ord(str1[s1]) + 1 == ord(str2[s2]) or
                ord(str1[s1]) - 25 == ord(str2[s2])):
                s2 += 1
        return s2 == len(str2)
            
        