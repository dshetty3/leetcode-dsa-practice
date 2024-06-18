class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        s = set()
        c = Counter(arr)

        for i in c.values():
            if i not in s:
                s.add(i)
            else:
                return False
        return True 
        