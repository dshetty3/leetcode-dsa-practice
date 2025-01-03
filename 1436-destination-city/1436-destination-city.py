class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        s = set()
        for p in paths:
            s.add(p[0])
        
        for p in paths:
            if p[1] not in s:
                return p[1]
        