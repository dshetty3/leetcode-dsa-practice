class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix = [0] #initialize it by zero so that starts from 0, 1, 2, 3

        for n in arr:
            prefix.append(prefix[-1] ^ n)

        res = []
        for left, right in queries:
            res.append(prefix[right + 1] ^ prefix[left]) 
        return res