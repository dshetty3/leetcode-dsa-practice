class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # max_product = float('-inf')
        # cur_product = nums[0]

        # if 0 in nums:
        #     return 0 

        # cur_product = nums[0] * nums[1] * nums[2]
        # max_product = max(max_product, cur_product)

        # for n in nums:
        #     if n < 0:
        #         max_product = -1 * max_product
            
        # return max_product

        nums.sort()

        max_product1 = nums[-1] * nums[-2] * nums[-3]
        max_product2 = nums[0] * nums[1] * nums[-1]

        return max(max_product1, max_product2)





        