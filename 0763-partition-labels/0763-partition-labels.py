class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        indexMap = {}

        for i, c in enumerate(s):
            indexMap[c] = i
        
        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, indexMap[c])

            if i == end:
                res.append(size) 
                size = 0

        return res
        