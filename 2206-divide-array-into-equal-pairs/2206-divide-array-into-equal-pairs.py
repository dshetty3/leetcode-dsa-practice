class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        unpaired = set()

        for n in nums:
            if n not in unpaired:
                unpaired.add(n)
            else:
                unpaired.remove(n)
        
        return not unpaired

        # count = Counter(nums)

        # for count in count.values():
        #     if count % 2 == 0:
        #         return True
        #     return False



        