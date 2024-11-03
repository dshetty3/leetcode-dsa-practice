class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) == len(goal) and s in goal + goal:
            return True
        else:
            return False
        