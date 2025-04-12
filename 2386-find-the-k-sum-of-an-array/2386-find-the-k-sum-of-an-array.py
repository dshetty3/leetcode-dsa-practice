import heapq

class Solution:
    def kSum(self, nums, k):
        max_sum = sum(x for x in nums if x > 0)
        nums = sorted(abs(x) for x in nums)
        n = len(nums)

        # Edge case: if k == 1, return max_sum
        if k == 1:
            return max_sum

        heap = [(-(max_sum - nums[0]), 0)]
        visited = set()
        visited.add((0,))
        count = 1  # We've already considered max_sum

        while heap:
            curr_sum, i = heapq.heappop(heap)
            count += 1
            if count == k:
                return -curr_sum

            if i + 1 < n:
                # Case 1: subtract next number
                new1 = (-( -curr_sum - nums[i + 1]), i + 1)
                if new1 not in visited:
                    heapq.heappush(heap, new1)
                    visited.add(new1)

                # Case 2: replace current with next
                new2 = (-( -curr_sum - nums[i + 1] + nums[i]), i + 1)
                if new2 not in visited:
                    heapq.heappush(heap, new2)
                    visited.add(new2)

        return 0  # fallback if k is too large
