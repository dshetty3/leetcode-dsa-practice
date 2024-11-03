class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        s = ''

        for c in address:
            if c == '.':
                s += c.replace('.', '[.]')
            else:
                s += c
        return s        