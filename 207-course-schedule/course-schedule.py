class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        g = defaultdict(list)
        courses = prerequisites
        for a,b in courses:
            g[a].append(b)
        
        UNSEEN = 0
        VISITING = 1
        VISITED = 2
        states = [UNSEEN] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            elif state == VISITING: return False

            states[node] = VISITING
            for n in g[node]:
                if not dfs(n): return False
            
            states[node] = VISITED
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        


        