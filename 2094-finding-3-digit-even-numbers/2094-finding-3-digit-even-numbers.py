class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i == j or j == k or i == k:
                        continue
                    
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        
        res = sorted(list(nums))
        return res


        