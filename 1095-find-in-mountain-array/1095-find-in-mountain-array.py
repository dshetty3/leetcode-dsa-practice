# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """

        length = mountain_arr.length()

        l = 1
        r = length - 1 #beacause peak wont be on the edges heance shrink the window size by 1

        #find peak
        while l <= r:
            m = (l + r) // 2
            left = mountain_arr.get(m - 1)
            mid = mountain_arr.get(m)
            right = mountain_arr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m
        

        #left sorted

        l = 0
        r = peak

        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        #right sorted

        l = peak
        r = length - 1

        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val < target:
                r = m - 1
            elif val > target:
                l = m + 1
            else:
                return m
        return -1
            





        