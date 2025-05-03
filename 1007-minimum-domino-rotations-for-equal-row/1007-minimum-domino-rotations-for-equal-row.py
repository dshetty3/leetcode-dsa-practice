class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        def getRotations(tops, bottoms, target):
            r = 0
            for i in range(len(tops)):
                if tops[i] == target:
                    continue
                if bottoms[i] == target:
                    r += 1
                else:
                    return float('inf')
            return r

        res = float('inf')
        for i in range(1, 7):
            res = min(res, getRotations(tops, bottoms, i))
            res = min(res, getRotations(bottoms, tops, i))
        return -1 if res == float('inf') else res

        

    