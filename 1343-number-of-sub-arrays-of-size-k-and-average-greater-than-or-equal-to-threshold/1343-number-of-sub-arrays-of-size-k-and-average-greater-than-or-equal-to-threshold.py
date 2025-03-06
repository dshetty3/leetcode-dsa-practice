class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        res = 0
        l = 0
        r = 0
        curr_sum = 0
        
        while r < len(arr):
            curr_sum += arr[r]
            if r - l + 1 == k:
                if (curr_sum / k) >= threshold:
                    res += 1
                curr_sum -= arr[l]
                l += 1
            r += 1
        return res






            

        