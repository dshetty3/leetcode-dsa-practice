class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0 or k > len(nums):
            return False
        
        target = total // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(i, k, currSum):
            if k == 0:
                return True
            if currSum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or currSum + nums[j] > target or (j > 0 and nums[j] == nums[j-1] and not used[j-1]):
                    continue
                used[j] = True
                if backtrack(j + 1, k, currSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)
