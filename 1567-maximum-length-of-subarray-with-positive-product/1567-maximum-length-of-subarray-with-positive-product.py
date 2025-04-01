class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = nums[0]
        # prefix = 1
        # postfix = 1

        # for i in range(len(nums)):
        #     prefix = nums[i] * (prefix)
        #     postfix = nums[len(nums) - 1 - i] * postfix
        #     temp = max(prefix, postfix)
        #     res = max(res, temp)
        # return res

        pos = neg = ans = 0

        for n in nums:
            if n > 0:
                pos += 1
                neg += 1 if neg else 0
            elif n < 0:
                pos, neg = neg + 1 if neg else 0, pos + 1
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans



        
        