class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """

        changes = 0
        last = s[0].lower()

        for i in s[1:]:
            if i.lower() != last:
                changes += 1 
                last = i.lower()
        return changes
        