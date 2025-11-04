class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        res = []
        n = len(nums)
        for i in range(n - k + 1):
            count = Counter(nums[i : i + k])

            if len(count) <= x:
                res.append(sum(nums[i:i + k]))
            else:
                pairs = list(count.items())
                pairs.sort(key = lambda p : (p[1], p[0]), reverse = True)
                curr_sum = 0
                for n, count in pairs[:x]:
                    curr_sum += (n * count)
                res.append(curr_sum)
        return res

        