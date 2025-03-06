class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop() 
            for n in rooms[node]: 
                if not seen[n]:
                    seen[n] = True
                    stack.append(n)
        return all(seen)      