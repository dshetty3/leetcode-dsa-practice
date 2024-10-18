class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        

        res = []
        hashSet = set()
        for n in nums:
            if n in hashSet:
                res.append(n)
            hashSet.add(n)
        return res