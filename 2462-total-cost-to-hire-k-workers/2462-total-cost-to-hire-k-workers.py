class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        head = costs[:candidates]
        tail = costs[max(candidates, len(costs) - candidates):]
        
        heapify(head)
        heapify(tail)

        res = 0
        head_p = candidates
        tail_p = len(costs) - 1 - candidates

        for _ in range(k):
            if not tail or head and head[0] <= tail[0]:
                res += heapq.heappop(head)
                if head_p <= tail_p:
                    heapq.heappush(head, costs[head_p])
                    head_p += 1
            else:
                res += heapq.heappop(tail)
                if head_p <= tail_p:
                    heapq.heappush(tail, costs[tail_p])
                    tail_p -= 1
        return res

        