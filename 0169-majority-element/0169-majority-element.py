class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        

        max_val = -1
        ans = 0

        for key,val in count.items():
            if val > max_val:
                max_val = val
                ans = key
        return ans
        