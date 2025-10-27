class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        prev = 0
        res = 0

        for s in bank:
            count = 0
            for i in range(len(s)):
                if s[i] == '1':
                    count += 1
            
            if count > 0:
                res += prev * count
                prev = count
        return res
        