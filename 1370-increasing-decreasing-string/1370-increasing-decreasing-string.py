class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        char = 'abcdefghijklmnopqrstuvwxyz'

        while s:
            for c in char:
                if c in s:
                    res.append(c)
                    s = s.replace(c,'',1)
                else:
                    char = char.replace(c,'')
            char = char[::-1]
        return ''.join(res)
                