class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """

        count1, count2 = defaultdict(int), defaultdict(int)

        for n1, n2 in zip(target, arr):
            count1[n1] += 1
            count2[n2] += 1
        
        if len(count1) != len(count2):
            return False
        
        for n in count1:
            if count1[n] != count2[n]:
                return False
        return True
        