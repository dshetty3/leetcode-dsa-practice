class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        count = {}

        for s in arr:
            if s not in count:
                count[s] = 0
            count[s] += 1
        
        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""

        