class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        res = 0
        UNSEEN = 0
        VISITED = 1
        visit = [UNSEEN] * len(isConnected)

        def dfs(node):
            visit[node] = VISITED
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visit[i]:
                    dfs(i)
        
        for i in range(len(isConnected)):
            if not visit[i]:
                res += 1
                dfs(i)
        return res

        
        