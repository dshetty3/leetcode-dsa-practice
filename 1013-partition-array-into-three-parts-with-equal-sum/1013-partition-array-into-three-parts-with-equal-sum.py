class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        total = sum(arr)
        if (total % 3 != 0):
            return False

        target_sum = total // 3
        curr_sum = parts = 0

        for num in arr:
            curr_sum += num
            if curr_sum == target_sum:
                parts += 1
                curr_sum = 0
                if parts == 3:
                    return True
        
        return False




        
        