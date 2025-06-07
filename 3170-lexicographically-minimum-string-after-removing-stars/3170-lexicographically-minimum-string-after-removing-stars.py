class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxHeap = []
        removeIdx = set()
        for i, c in enumerate(s):
            if c == '*':
                c = heapq.heappop(maxHeap)
                removeIdx.add(i)
                removeIdx.add(-c[1])
                continue
            
            heapq.heappush(maxHeap, [c, -i])
        
        res = ""
        for i, c in enumerate(s):
            if i not in removeIdx:
                res += c
        return res


        