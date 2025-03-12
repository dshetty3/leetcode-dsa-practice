class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # TC - O(E + V)
        # SP - O(E + V)

        order = []
        g = defaultdict(list)
        courses = prerequisites

        for a, b in courses:
            g[a].append(b)
        

        UNSEEN, VISITING, VISITED = 0, 1, 2
        states = [UNSEEN] * numCourses

        def dfs(i):
            if states[i] == VISITED: 
                return True
            elif states[i] == VISITING: 
                return False
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei): return False

            states[i] = VISITED
            order.append(i)
            return order

        for i in range(numCourses):
            if not dfs(i): 
                return []
                
        return order



        