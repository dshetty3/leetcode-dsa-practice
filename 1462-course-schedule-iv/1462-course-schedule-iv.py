class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        order = []
        g = defaultdict(list)

        courses = prerequisites

        for a,b in courses:
            g[a].append(b)
        
        UNSEEN, VISITING, VISITED = 0, 1, 2
        states = [UNSEEN] * numCourses
        pre_req = [[False] * numCourses for _ in range(numCourses)]

        def dfs(node):
            if states[node] == VISITED: return True
            if states[node] == VISITING: return False

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False
                for i in range(numCourses):
                    if pre_req[nei][i]:
                        pre_req[node][i] = True
                pre_req[node][nei] = True
            

            states[node] = VISITED
            order.append(node)
            return True
        
        for i in range(numCourses):
            if states[i] == UNSEEN:
                dfs(i)
        
        return [pre_req[a][b] for a, b in queries]
                


        