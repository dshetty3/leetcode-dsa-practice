class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # if s.count('A') >= 2:
        #     return False
        # if 'LLL' in s:
        #     return False
        # return True

        countA = 0
        countL = 0

        for i in s:
            if i == 'A':
                countA += 1
            if i == 'L': 
                countL += 1
            else:
                countL = 0
            
            if countA >= 2 or countL >= 3:
                return False
        return True
        