class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        seen = [False] * len(rooms)
        seen[0] = True
        q = deque([0])

        while q:
            node = q.popleft() 
            for n in rooms[node]: 
                if not seen[n]:
                    seen[n] = True
                    q.append(n)
        return all(seen)      