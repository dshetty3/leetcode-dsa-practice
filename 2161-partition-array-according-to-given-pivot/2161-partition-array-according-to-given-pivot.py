class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
        num1 = []
        pivot1 = []
        num2 = []

        for n in nums:
            if n < pivot:
                num1.append(n)
            elif n > pivot:
                num2.append(n)
            else:
                pivot1.append(n) 
        res = num1 + pivot1 + num2
        return res