class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        first = last = 0

        for n in derived:
            if n:
                last = ~last
        return first == last
        
        



        