class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        l = 0
        r = len(arr) - 1

        if len(arr) > 2:
            while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]:
                l += 1
            while r - 1 > 0 and arr[r] < arr[r - 1]:
                r -= 1
            return l == r
        return False
        


        