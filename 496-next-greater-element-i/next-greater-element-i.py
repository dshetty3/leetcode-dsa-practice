class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #convert nums1 to hashmap for index and val
        nums1Index = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)): #iterate the secoond loop
            curr = nums2[i]
            while stack and curr > stack[-1]: #curr val is greater than stack[-1]
                val = stack.pop() #pop it out of the stack
                idx = nums1Index[val] #get the index of the poped value from nums1
                res[idx] = curr #add the curr value to the index of res
            if curr in nums1Index:
                stack.append(curr)
        return res
        