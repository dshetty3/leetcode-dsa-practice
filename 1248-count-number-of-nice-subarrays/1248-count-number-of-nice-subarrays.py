class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            l = 0
            res = 0
            odd = 0


            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    odd += 1
            
                while odd > k:
                    if nums[l] % 2 == 1:
                        odd -= 1
                    l += 1
                
                res += (r - l) + 1
            return res

        return atMost(k) - atMost(k - 1)

        
        