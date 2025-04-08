class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0

        for i in range(0, len(nums), 3):
            seen = set()
            unique = True
            for n in nums[i:]:
                if n in seen:
                    unique = False
                    break
                seen.add(n)
            if unique:
                return ans
            ans += 1
        return ans 

        

