class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        count = {} 
        # 3: 2, 2: 1
        l = len(nums) // 3

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        res = []        
        
        for key , val in count.items():
            if val > l:
                res.append(key)
        return res
        

        