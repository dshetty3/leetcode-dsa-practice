class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        
        charSet = set()

        def overlap(charSet, s):
            unique = set()
            for c in s:
                if c in charSet or c in unique:
                    return True
                unique.add(c)
            return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):
                #include
                for c in arr[i]:
                    charSet.add(c)
                #backtrack    
                res = backtrack(i + 1)
                #exclude
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))
        return backtrack(0)



