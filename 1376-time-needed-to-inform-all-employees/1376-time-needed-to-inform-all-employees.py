class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """

        adj = defaultdict(list)

        for i in range(n):
            adj[manager[i]].append(i)
        
        q = deque([(headID, 0)]) #id, time
        res = 0
        while q:
            i, time = q.popleft()
            res = max(res, time)

            for emp in adj[i]:
                q.append((emp, time + informTime[i]))
        return res

        