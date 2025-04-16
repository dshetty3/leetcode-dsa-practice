class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        l = 0
        count = 0
        seen = Counter()
        pairs = 0

        for r in range(len(nums)):
            pairs += seen[nums[r]]
            seen[nums[r]] += 1


            while pairs >= k:
                seen[nums[l]] -= 1
                pairs -= seen[nums[l]]
                l += 1

            count += l
        
        return count


        